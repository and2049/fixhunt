// Minimal OpenAI-compatible chat client with JSON-schema output and a spend log.
import { LLM, RUNS_DIR } from "./config";
import { appendFileSync, mkdirSync } from "node:fs";

export type Msg = { role: "system" | "user" | "assistant"; content: string };

export type ChatOpts = {
  model: string;
  messages: Msg[];
  schema?: { name: string; schema: Record<string, unknown> };
  maxTokens?: number;
  temperature?: number;
  think?: boolean; // Nemotron reasoning; off by default for structured stages
  tag?: string; // stage name for the spend log
};

export type Usage = { prompt: number; completion: number; reasoning: number };

const PRICES: Record<string, [number, number]> = {
  // $ per 1M tokens, input / output; verify against the Token Factory console
  "nvidia/Nemotron-3_5-Lightning": [0.06, 0.24],
  "nvidia/nemotron-3-super-120b-a12b": [0.3, 0.9],
  "nvidia/Nemotron-3-Ultra-550b-a55b": [1, 3],
  "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B": [0.06, 0.24],
};

export function costOf(model: string, u: Usage): number {
  const p = PRICES[model];
  if (!p) return 0;
  return (u.prompt * p[0] + u.completion * p[1]) / 1e6;
}

export async function chat(opts: ChatOpts): Promise<{ text: string; usage: Usage; cost: number }> {
  if (!LLM.apiKey) throw new Error("NEBIUS_API_KEY is not set");
  const body: Record<string, unknown> = {
    model: opts.model,
    messages: opts.messages,
    max_tokens: opts.maxTokens ?? 4096,
    temperature: opts.temperature ?? 0.7,
  };
  if (!opts.think) {
    // Both forms are accepted by Token Factory for Nemotron; keep both for safety.
    body.chat_template_kwargs = { enable_thinking: false };
    body.reasoning_effort = "none";
  }
  if (opts.schema) {
    body.response_format = { type: "json_schema", json_schema: { name: opts.schema.name, schema: opts.schema.schema } };
  }

  let lastErr: unknown;
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const res = await fetch(`${LLM.baseUrl}chat/completions`, {
        method: "POST",
        headers: { "content-type": "application/json", authorization: `Bearer ${LLM.apiKey}` },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(180_000),
      });
      if (res.status === 429 || res.status >= 500) {
        lastErr = new Error(`${res.status} ${await res.text()}`);
        await Bun.sleep(1500 * 2 ** attempt);
        continue;
      }
      if (!res.ok) throw new Error(`LLM ${res.status}: ${await res.text()}`);
      const data: any = await res.json();
      const text: string = data.choices?.[0]?.message?.content ?? "";
      // Token Factory occasionally returns a provider-side failure as the message body; treat it as transient
      if (!text || /^\[ERROR:/.test(text.trim()) || data.choices?.[0]?.finish_reason === "error") {
        lastErr = new Error(`provider error: ${text.slice(0, 200) || "empty completion"}`);
        await Bun.sleep(1500 * 2 ** attempt);
        continue;
      }
      const u = data.usage ?? {};
      const usage: Usage = {
        prompt: u.prompt_tokens ?? 0,
        completion: u.completion_tokens ?? 0,
        reasoning: u.completion_tokens_details?.reasoning_tokens ?? 0,
      };
      const cost = costOf(opts.model, usage);
      logSpend({ ts: new Date().toISOString(), tag: opts.tag ?? "", model: opts.model, ...usage, cost });
      return { text, usage, cost };
    } catch (e) {
      lastErr = e;
      if (attempt === 3) break;
      await Bun.sleep(1500 * 2 ** attempt);
    }
  }
  throw lastErr instanceof Error ? lastErr : new Error(String(lastErr));
}

export async function chatJson<T>(opts: ChatOpts): Promise<{ value: T; usage: Usage; cost: number }> {
  let usage: Usage = { prompt: 0, completion: 0, reasoning: 0 };
  let cost = 0;
  let last = "";
  for (let attempt = 0; attempt < 3; attempt++) {
    const r = await chat(attempt === 0 ? opts : { ...opts, temperature: Math.min(1, (opts.temperature ?? 0.7) + 0.1 * attempt) });
    usage = { prompt: usage.prompt + r.usage.prompt, completion: usage.completion + r.usage.completion, reasoning: usage.reasoning + r.usage.reasoning };
    cost += r.cost;
    const value = parseJsonLoose<T>(r.text);
    if (value !== undefined) return { value, usage, cost };
    last = r.text;
  }
  throw new Error(`model did not return JSON (${opts.tag}) after 3 attempts: ${last.slice(0, 300)}`);
}

/** Parse a JSON object out of model text: strips code fences and leading prose, tolerates trailing text. */
export function parseJsonLoose<T>(raw: string): T | undefined {
  const text = raw.trim().replace(/^```(?:json)?\s*|\s*```$/g, "");
  try { return JSON.parse(text) as T; } catch {}
  const start = text.indexOf("{");
  if (start < 0) return undefined;
  // scan for the matching close brace, respecting strings
  let depth = 0, inStr = false, esc = false;
  for (let i = start; i < text.length; i++) {
    const c = text[i];
    if (inStr) { if (esc) esc = false; else if (c === "\\") esc = true; else if (c === '"') inStr = false; continue; }
    if (c === '"') inStr = true;
    else if (c === "{") depth++;
    else if (c === "}") { depth--; if (depth === 0) { try { return JSON.parse(text.slice(start, i + 1)) as T; } catch { return undefined; } } }
  }
  return undefined;
}

export function logSpend(row: Record<string, unknown>) {
  try {
    mkdirSync(RUNS_DIR, { recursive: true });
    appendFileSync(`${RUNS_DIR}/spend.jsonl`, JSON.stringify(row) + "\n");
  } catch {}
}
