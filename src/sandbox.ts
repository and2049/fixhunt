// Process execution. Trusted tools (linters, parsers) run locally with a timeout. Generated programs
// (`isolate: true`) run in Token Factory Sandboxes when available, else under bubblewrap, else plain.
// FIXHUNT_SANDBOX=contree|bwrap|auto (default auto).

import { resolve } from "node:path";
import { AsyncLocalStorage } from "node:async_hooks";
import { contreeStatus, runInSandbox } from "./contree";

export type ExecResult = { stdout: string; stderr: string; code: number | null; timedOut: boolean; signal?: string };

let bwrapOk: boolean | null = null;

export async function detectBwrap(): Promise<boolean> {
  if (bwrapOk !== null) return bwrapOk;
  try {
    const p = Bun.spawn(["bwrap", "--unshare-net", "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc", "true"], {
      stdout: "ignore",
      stderr: "ignore",
    });
    bwrapOk = (await p.exited) === 0;
  } catch {
    bwrapOk = false;
  }
  return bwrapOk;
}

const MODE = (process.env.FIXHUNT_SANDBOX ?? "auto").toLowerCase();

const policy = new AsyncLocalStorage<{ localOnly: boolean }>();
/** Run `fn` with generated-program execution forced local (bwrap) for this async context only. Used by
 * minimization, which needs dozens of evaluations per finding; the minimized result is then confirmed in a real sandbox. */
export function withLocalSandbox<T>(fn: () => Promise<T>): Promise<T> {
  return policy.run({ localOnly: true }, fn);
}

export async function useContree(): Promise<boolean> {
  if (MODE === "bwrap" || MODE === "none" || (policy.getStore()?.localOnly && MODE !== "contree-always")) return false;
  const s = await contreeStatus();
  if (!s.ok && MODE === "contree") throw new Error(`FIXHUNT_SANDBOX=contree but sandboxes are unavailable: ${s.why}`);
  return s.ok;
}

export async function sandboxInfo(net = false): Promise<string> {
  if (await useContree()) return `Token Factory Sandboxes (fresh VM per run, ${net ? "network on" : "no network"})`;
  const s = await contreeStatus();
  const why = MODE === "auto" && s.why ? ` (sandboxes unavailable: ${s.why})` : "";
  return (await detectBwrap()) ? `bwrap (no network, read-only root)${why}` : `plain process (no isolation beyond timeout)${why}`;
}

export async function exec(cmd: string[], opts: { cwd: string; timeoutMs?: number; isolate?: boolean; image?: string; env?: Record<string, string>; maxOutput?: number; net?: boolean; recursive?: boolean; exclude?: string[] }): Promise<ExecResult> {
  const timeoutMs = opts.timeoutMs ?? 5000;
  const cwd = resolve(opts.cwd);
  if (opts.isolate && opts.image && (await useContree())) {
    try {
      const r = await runInSandbox(cmd, { image: opts.image, cwd, env: opts.env, timeoutMs, maxOutput: opts.maxOutput, net: opts.net, recursive: opts.recursive, exclude: opts.exclude });
      return { stdout: cap(r.stdout, opts.maxOutput), stderr: cap(r.stderr, opts.maxOutput), code: r.code, timedOut: r.timedOut, signal: r.signal };
    } catch (e) {
      return { stdout: "", stderr: `sandbox failure: ${String((e as Error).message ?? e)}`, code: null, timedOut: false };
    }
  }
  let argv = cmd;
  let env: Record<string, string | undefined> = { ...process.env, ...opts.env };
  if (opts.isolate) {
    if (!(await detectBwrap())) {
      if (MODE !== "none") return { stdout: "", stderr: "sandbox failure: no isolation available (install bwrap, enable Token Factory Sandboxes, or set FIXHUNT_SANDBOX=none to run generated programs as plain processes)", code: null, timedOut: false };
    } else {
      // Read-only root, no network, no home directories, no inherited secrets: a clean environment with the working directory writable
      const home = process.env.HOME;
      argv = [
        "bwrap", ...(opts.net ? [] : ["--unshare-net"]), "--unshare-pid", "--die-with-parent", "--new-session",
        "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc", "--tmpfs", "/tmp", "--tmpfs", "/root", ...(home && home !== "/" ? ["--tmpfs", home] : []),
        "--bind", cwd, cwd, "--chdir", cwd,
        ...cmd,
      ];
      env = { PATH: process.env.PATH ?? "/usr/local/bin:/usr/bin:/bin", HOME: "/tmp", LANG: "C.UTF-8", LC_ALL: "C.UTF-8", TMPDIR: "/tmp", ...opts.env };
    }
  }
  const p = Bun.spawn(argv, { cwd, stdout: "pipe", stderr: "pipe", env });
  let timedOut = false;
  const timer = setTimeout(() => {
    timedOut = true;
    try { p.kill("SIGKILL"); } catch {}
  }, timeoutMs);
  // Collect output incrementally. After the process exits (or is killed) wait only briefly for the
  // streams: a killed process can leave a pipe that never reports EOF, which would hang us forever.
  const limit = (opts.maxOutput ?? 64 * 1024) * 2;
  const overflow = () => { try { p.kill("SIGKILL"); } catch {} };
  const out = collect(p.stdout, limit, overflow);
  const err = collect(p.stderr, limit, overflow);
  const code = await p.exited;
  clearTimeout(timer);
  await Promise.race([Promise.all([out.done, err.done]), Bun.sleep(2000)]);
  return { stdout: cap(out.text(), opts.maxOutput), stderr: cap(err.text(), opts.maxOutput), code: timedOut ? null : code, timedOut, signal: p.signalCode == null ? undefined : String(p.signalCode) };
}

/** Collect a stream up to `limit` bytes; past that, stop reading and call `onOverflow` (which kills the process). */
function collect(stream: ReadableStream<Uint8Array>, limit = Infinity, onOverflow?: () => void): { done: Promise<void>; text: () => string } {
  const chunks: Uint8Array[] = [];
  let size = 0;
  const done = (async () => {
    const reader = stream.getReader();
    try {
      for (;;) {
        const { value, done } = await reader.read();
        if (done) break;
        if (value) { chunks.push(value); size += value.length; if (size > limit) { onOverflow?.(); try { await reader.cancel(); } catch {} break; } }
      }
    } catch {}
  })();
  return { done, text: () => new TextDecoder().decode(concat(chunks)) };
}

function concat(chunks: Uint8Array[]): Uint8Array {
  const n = chunks.reduce((a, c) => a + c.length, 0);
  const out = new Uint8Array(n);
  let o = 0;
  for (const c of chunks) { out.set(c, o); o += c.length; }
  return out;
}

function cap(s: string, n = 64 * 1024): string {
  return s.length > n ? s.slice(0, n) + `\n...[truncated ${s.length - n} bytes]` : s;
}
