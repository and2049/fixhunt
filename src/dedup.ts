// Stage 6: DEDUP. Search upstream issues (GitHub) and the web (Tavily) for the same symptom.
import { chatJson } from "./llm";
import { MODELS } from "./config";

export type Hit = { source: "github" | "tavily"; title: string; url: string; state?: string; snippet?: string };
export type DedupResult = { queries: string[]; hits: Hit[]; verdicts: Array<{ url: string; relation: "duplicate" | "related" | "unrelated"; why: string }>; cost: number };

// Upstream repositories come from the tool spec (`repo`); `tool` below is the "owner/name" string.

async function ghToken(): Promise<string | undefined> {
  if (process.env.GITHUB_TOKEN) return process.env.GITHUB_TOKEN;
  try {
    const p = Bun.spawn(["gh", "auth", "token"], { stdout: "pipe", stderr: "ignore" });
    const t = (await new Response(p.stdout).text()).trim();
    return (await p.exited) === 0 && t ? t : undefined;
  } catch { return undefined; }
}

export async function searchGithub(repo: string | undefined, q: string): Promise<Hit[]> {
  if (!repo) return [];
  const token = await ghToken();
  const url = `https://api.github.com/search/issues?per_page=10&q=${encodeURIComponent(`repo:${repo} is:issue ${q}`)}`;
  const res = await fetch(url, { headers: { accept: "application/vnd.github+json", ...(token ? { authorization: `Bearer ${token}` } : {}) }, signal: AbortSignal.timeout(20_000) });
  if (!res.ok) return [];
  const data: any = await res.json();
  return (data.items ?? []).map((it: any) => ({ source: "github" as const, title: it.title, url: it.html_url, state: it.state, snippet: (it.body ?? "").slice(0, 300) }));
}

export async function searchTavily(q: string): Promise<Hit[]> {
  const key = process.env.TAVILY_API_KEY;
  if (!key) return [];
  const res = await fetch("https://api.tavily.com/search", {
    method: "POST",
    headers: { "content-type": "application/json", authorization: `Bearer ${key}` },
    body: JSON.stringify({ query: q, max_results: 8, search_depth: "basic" }),
    signal: AbortSignal.timeout(30_000),
  });
  if (!res.ok) return [];
  const data: any = await res.json();
  return (data.results ?? []).map((r: any) => ({ source: "tavily" as const, title: r.title ?? "", url: r.url, snippet: (r.content ?? "").slice(0, 300) }));
}

export type DedupInput = { tool: string; repo?: string; rule: string; kind: string; observed: string; repro: string; diff: string };

export async function dedup(inp: DedupInput): Promise<DedupResult> {
  const { tool, rule } = inp;
  const short = rule.split("/").pop()!;
  let cost = 0;
  const finding = `Tool ${tool}, rule ${rule}. Oracle: ${inp.kind}.\nProgram:\n${inp.repro}\nDiff applied by the fix:\n${inp.diff}\nObserved:\n${inp.observed}`;
  // 1. Ask for search queries that name the construct, not the symptom wording
  let queries = [`${short} fix`];
  try {
    const q = await chatJson<{ queries: string[] }>({
      model: MODELS.mid,
      messages: [
        { role: "system", content: "You write issue-tracker search queries for linter autofix bugs. Queries are 3-8 words naming the rule and the code construct involved (e.g. the statement shape, keyword, or API), never the words 'before', 'after', 'stdout'." },
        { role: "user", content: `${finding}\n\nReturn JSON {"queries":["...","...","..."]} with three distinct queries.` },
      ],
      maxTokens: 300,
      temperature: 0.3,
      tag: "dedup-queries",
    });
    cost += q.cost;
    queries = [...queries, ...(q.value.queries ?? []).map(String).filter(Boolean).slice(0, 3)];
  } catch {}
  // 2. Search GitHub directly plus Tavily restricted to the tracker (the bonus requires a runtime Tavily call)
  const hits: Hit[] = [];
  const seen = new Set<string>();
  const repo = inp.repo;
  for (const q of queries) {
    const gh = await searchGithub(repo, q);
    const tv = await searchTavily(`${q} site:github.com/${repo ?? ""}`);
    for (const h of [...gh, ...tv]) {
      h.url = h.url.replace(/[?#].*$/, "").replace(/\/(commits|files|checks)$/, "");
      if (seen.has(h.url) || !/^https:\/\/github\.com\/[^/]+\/[^/]+\/(issues|pull)\/\d+$/.test(h.url)) continue;
      seen.add(h.url);
      hits.push(h);
    }
  }
  if (!hits.length) return { queries, hits, verdicts: [], cost };
  // 3. Triage with the judge model: duplicate means the existing report's own reproducer exercises the same defect
  const r = await chatJson<{ verdicts: Array<{ url: string; relation: string; why: string }> }>({
    model: MODELS.judge,
    messages: [
      { role: "system", content: "You triage bug reports for a linter autofix. Be strict: 'duplicate' only if the existing report describes the same defect, meaning the same rewrite going wrong on the same kind of construct, so that fixing the existing report would also fix the new finding. 'related' means same rule or same class of defect but a different construct or cause. Otherwise 'unrelated'. Titles and snippets are all you have; when a snippet does not show the construct, prefer 'related' over 'duplicate'." },
      { role: "user", content: `New finding:\n${finding}\n\nExisting reports:\n${hits.map((h, i) => `${i + 1}. [${h.source}${h.state ? ", " + h.state : ""}] ${h.title}\n   ${h.url}\n   ${h.snippet?.replace(/\s+/g, " ")}`).join("\n")}\n\nReturn JSON {"verdicts":[{"url":"...","relation":"duplicate|related|unrelated","why":"one sentence naming the construct in the existing report"}]} with one entry per report.` },
    ],
    maxTokens: 3000,
    temperature: 0.1,
    tag: "dedup",
  });
  cost += r.cost;
  const known = new Set(hits.map((h) => h.url));
  // Only URLs that the searches actually returned; the model may not introduce links
  const verdicts = (r.value.verdicts ?? []).filter((v) => known.has(String(v.url))).map((v) => ({ url: String(v.url), relation: (["duplicate", "related", "unrelated"].includes(v.relation) ? v.relation : "unrelated") as any, why: String(v.why ?? "") }));
  return { queries, hits, verdicts, cost };
}
