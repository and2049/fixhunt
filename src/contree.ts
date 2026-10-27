// Token Factory Sandboxes (Contree) client: run one command in a fresh, disposable, network-less VM.
// The working directory is shipped as a gzipped tarball on stdin, so no upload step and no image preparation.
import { readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";
import { LLM, RUNS_DIR } from "./config";
import { logSpend } from "./llm";
import type { ExecResult } from "./sandbox";

const BASE = (process.env.NEBIUS_SANDBOX_URL ?? "https://api.tokenfactory.nebius.com/sandboxes/v1").replace(/\/$/, "");
const PROJECT = process.env.NEBIUS_PROJECT_ID ?? "";

export type SandboxLimits = { instance_max_timeout: number; instance_max_concurrency: number };
let whoami: Promise<{ ok: boolean; limits?: SandboxLimits; why?: string }> | undefined;

function headers(): Record<string, string> {
  return { authorization: `Bearer ${LLM.apiKey}`, project: PROJECT, "content-type": "application/json" };
}

/** True when the key has sandbox spawn permission (cached for the process). */
export function contreeStatus(): Promise<{ ok: boolean; limits?: SandboxLimits; why?: string }> {
  if (whoami) return whoami;
  whoami = (async () => {
    if (!LLM.apiKey || !PROJECT) return { ok: false, why: "NEBIUS_API_KEY or NEBIUS_PROJECT_ID not set" };
    try {
      const r = await fetch(`${BASE}/whoami`, { headers: headers(), signal: AbortSignal.timeout(15_000) });
      if (!r.ok) return { ok: false, why: `whoami ${r.status}` };
      const j: any = await r.json();
      if (!j.permissions?.spawn_disposable) return { ok: false, why: "sandbox permissions not granted (beta access pending)" };
      return { ok: true, limits: j.limits };
    } catch (e) {
      return { ok: false, why: String(e).slice(0, 120) };
    }
  })();
  return whoami;
}

export const shellQuote = (s: string) => `'${s.replace(/'/g, `'\\''`)}'`;

/** Tar `cwd` (regular files only, or the whole tree with `recursive`) and return it base64-encoded. */
async function packDir(cwd: string, recursive = false, exclude: string[] = []): Promise<string> {
  const files = recursive ? ["."] : readdirSync(cwd).filter((f) => { try { return statSync(join(cwd, f)).isFile(); } catch { return false; } });
  if (!files.length) return "";
  const p = Bun.spawn(["tar", "cz", "-C", cwd, ...exclude.flatMap((e) => ["--exclude", e]), ...(recursive ? [] : ["--no-recursion"]), "--", ...files], { stdout: "pipe", stderr: "pipe" });
  const buf = Buffer.from(await new Response(p.stdout).arrayBuffer());
  if ((await p.exited) !== 0) throw new Error("tar failed: " + (await new Response(p.stderr).text()));
  return buf.toString("base64");
}

export type SandboxOpts = { image: string; cwd: string; env?: Record<string, string>; timeoutMs?: number; maxOutput?: number; net?: boolean; recursive?: boolean; exclude?: string[] };

/** Run `cmd` in `image` with the files of `cwd` unpacked into /w. Throws on infrastructure failure. */
export async function runInSandbox(cmd: string[], o: SandboxOpts): Promise<ExecResult & { cost: number; opId: string }> {
  const tarb64 = await packDir(resolve(o.cwd), o.recursive, o.exclude);
  const MAX_ARCHIVE = Number(process.env.FIXHUNT_MAX_ARCHIVE_MB ?? 50) * 1024 * 1024;
  if (tarb64.length * 0.75 > MAX_ARCHIVE) throw new Error(`working directory archive exceeds ${MAX_ARCHIVE / 1024 / 1024} MB; exclude build artifacts or raise FIXHUNT_MAX_ARCHIVE_MB`);
  const inner = cmd.map(shellQuote).join(" ");
  const command = `mkdir -p /w && cd /w && ${tarb64 ? "base64 -d | tar xz && " : ""}exec ${inner}`;
  const timeout = Math.max(1, Math.ceil((o.timeoutMs ?? 5000) / 1000));
  const body = {
    image: o.image.startsWith("tag:") || /^[0-9a-f-]{36}$/.test(o.image) ? o.image : `tag:${o.image}`,
    command, shell: true, disposable: true, timeout, env: o.env ?? {},
    networking: { enabled: !!o.net }, truncate_output_at: Math.min(10 * 1024 * 1024, Math.max(65536, (o.maxOutput ?? 65536) * 2)),
    stdin: { value: tarb64, encoding: "ascii", close: true },
  };
  let opId = "";
  for (let attempt = 0; ; attempt++) {
    const r = await fetch(`${BASE}/instances`, { method: "POST", headers: headers(), body: JSON.stringify(body), signal: AbortSignal.timeout(60_000) });
    if (r.status === 201) { opId = ((await r.json()) as any).uuid; break; }
    const text = await r.text();
    if ((r.status === 429 || r.status >= 500) && attempt < 3) { await Bun.sleep(1000 * (attempt + 1)); continue; }
    throw new Error(`sandbox spawn failed: ${r.status} ${text.slice(0, 200)}`);
  }
  const deadline = Date.now() + timeout * 1000 + 120_000;
  for (;;) {
    if (Date.now() > deadline) throw new Error(`sandbox operation ${opId} did not finish in time`);
    let r: Response;
    try { r = await fetch(`${BASE}/operations/${opId}`, { headers: headers(), signal: AbortSignal.timeout(30_000) }); }
    catch { await Bun.sleep(1000); continue; }
    if (!r.ok) { if (r.status >= 500 || r.status === 429) { await Bun.sleep(1000); continue; } throw new Error(`sandbox status failed: ${r.status}`); }
    const j: any = await r.json();
    if (j.status === "SUCCESS" || j.status === "FAILED" || j.status === "CANCELLED") {
      const res = j.metadata?.result;
      if (!res) throw new Error(`sandbox operation ${j.status}: ${j.error ?? "no result"}`);
      const dec = (x: any) => (x?.encoding === "base64" ? Buffer.from(x.value ?? "", "base64").toString("utf8") : String(x?.value ?? ""));
      const cost = Number(res.resources?.cost ?? 0);
      logSpend({ ts: new Date().toISOString(), tag: "sandbox", model: "token-factory-sandboxes", prompt: 0, completion: 0, reasoning: 0, cost, seconds: res.resources?.monotonic_time, image: body.image, op: opId });
      const timedOut = !!res.state?.timed_out;
      return { stdout: dec(res.stdout), stderr: dec(res.stderr), code: timedOut ? null : Number(res.state?.exit_code ?? 0), timedOut, signal: res.state?.signal > 0 ? String(res.state.signal) : undefined, cost, opId };
    }
    const ra = Number(r.headers.get("retry-after"));
    await Bun.sleep(Number.isFinite(ra) && ra > 0 ? Math.min(ra * 1000, 2000) : 400);
  }
}

export const SANDBOX_LOG = `${RUNS_DIR}/spend.jsonl`;
