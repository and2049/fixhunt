// Dashboard server: hunts and repository scans with a streamed progress feed, findings, runs. Reads the same runs/ tree the CLI writes.
import { existsSync, mkdtempSync, readFileSync, realpathSync, rmSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve, sep } from "node:path";
import { RUNS_DIR } from "./config";
import { hunt, type HuntEvent } from "./hunt";
import { scan, type ScanEvent } from "./scan";
import { sweepRules } from "./catalog";
import { cloneRepo, parseRepoUrl, removeClone, subdir } from "./clone";
import type { Tool } from "./tools/types";
import type { SpecTool } from "./tools/spec";
import { catalogRules, findingByPath, findings, fixtureName, fixtureText, loadRuns, loadScans, scanFinding, spend, stats } from "./web/data";
import { evaluateProgram } from "./oracles";
import { sandboxInfo } from "./sandbox";
import { serverLinks } from "./web/html";
import { allow, charge, gated, lookup, remaining } from "./budget";
import { docsPage, findingPage, findingsPage, huntPage, runPage, runsPage, scanPage, scansPage } from "./web/pages";
import type { HuntPageData } from "./web/pages";

let TOOLS: Record<string, Tool> = {};
const L = serverLinks();
const TOKEN = process.env.FIXHUNT_TOKEN ?? ""; // when set, POST endpoints require `Authorization: Bearer <token>`
const MAX_RERUNS = Number(process.env.FIXHUNT_MAX_RERUNS ?? 2);
let rerunsInFlight = 0;
const HUNT_ESTIMATE = 0.15, RERUN_ESTIMATE = 0.01, SCAN_ESTIMATE = 0.1; // USD, checked against budgets before starting; actual spend is charged after
const MAX_N = Number(process.env.FIXHUNT_MAX_N ?? 10), MAX_ROUNDS = Number(process.env.FIXHUNT_MAX_ROUNDS ?? 2);
const SCAN_LIMIT = Number(process.env.FIXHUNT_SCAN_LIMIT ?? 30); // rules per dashboard scan
const SCAN_TIMEOUT_MS = Number(process.env.FIXHUNT_SCAN_TIMEOUT ?? 300) * 1000; // per command run
// Tools offered for dashboard scans. A scan runs the tool's fixer on a cloned repository on this host, so only tools whose
// configuration is data (not executable) belong here; ESLint loads eslint.config.js and must stay out on a public instance.
const SCAN_TOOLS = (process.env.FIXHUNT_SCAN_TOOLS ?? "").split(",").map((s) => s.trim()).filter(Boolean);
const scanTools = () => Object.keys(TOOLS).filter((t) => !SCAN_TOOLS.length || SCAN_TOOLS.includes(t));
// Rules a default scan would apply per tool (the fixes the tool labels safe), from the cached catalog
const sweepCache = new Map<string, number>();
function sweepCount(t: Tool): number {
  if (!sweepCache.has(t.id)) { try { const j = JSON.parse(readFileSync(`data/${t.id}-rules.json`, "utf8")); sweepCache.set(t.id, sweepRules(t as SpecTool, Array.isArray(j) ? j : j.rules, false).length); } catch { sweepCache.set(t.id, 0); } }
  return sweepCache.get(t.id)!;
}

function codeOf(req: Request): string | undefined {
  const m = /(?:^|;\s*)fixhunt_code=([^;]+)/.exec(req.headers.get("cookie") ?? "");
  return m ? decodeURIComponent(m[1]) : req.headers.get("x-fixhunt-code") ?? undefined;
}

type JobEvent = HuntEvent | ScanEvent | { type: "clone"; url: string; done: boolean; mb?: number; head?: string };
type Live = { id: string; kind: "hunt" | "scan"; events: JobEvent[]; listeners: Set<(e: JobEvent) => void>; done: boolean; started: number };
const jobs = new Map<string, Live>();
let running: Live | undefined;

const html = (s: string, status = 200) => new Response(s, { status, headers: { "content-type": "text/html; charset=utf-8" } });
const json = (o: unknown, status = 200) => new Response(JSON.stringify(o), { status, headers: { "content-type": "application/json" } });
const redirect = (to: string) => new Response(null, { status: 302, headers: { location: to } });

function newJob(kind: Live["kind"]): Live {
  const live: Live = { id: Math.random().toString(36).slice(2, 10), kind, events: [], listeners: new Set(), done: false, started: Date.now() };
  jobs.set(live.id, live);
  running = live;
  return live;
}
const emitter = (live: Live, onDone?: () => void) => (e: JobEvent) => {
  live.events.push(e);
  for (const l of live.listeners) l(e);
  if (e.type === "done" || e.type === "error") live.done = true;
  if (e.type === "done") onDone?.();
};
const firstLine = (e: unknown) => String((e as Error)?.message ?? e).split("\n")[0].slice(0, 300);

function startHunt(body: { tool: string; rule: string; n: number; rounds: number; unsafe: boolean }, code: string | undefined): { id: string } | { error: string } {
  const tool = TOOLS[body.tool];
  if (!tool) return { error: `unknown tool ${body.tool}` };
  const gate = allow(code, HUNT_ESTIMATE);
  if (!gate.ok) return { error: gate.reason };
  if (!body.rule || !/^[\w.:-]+(\/[\w.:-]+)*$/.test(body.rule) || body.rule.split("/").some((s) => s === "." || s === "..")) return { error: "rule id required" };
  if (running && !running.done) return { error: `a ${running.kind} is already running; wait for it to finish` };
  const live = newJob("hunt");
  const emit = emitter(live, () => { const d = live.events.find((e) => e.type === "done") as Extract<HuntEvent, { type: "done" }> | undefined; charge(gate.access.code, (d?.cost ?? 0) + 0.01); });
  hunt({ tool, rule: body.rule, n: Math.max(2, Math.min(MAX_N, body.n || 6)), rounds: Math.max(1, Math.min(MAX_ROUNDS, body.rounds || 1)), unsafe: !!body.unsafe, onEvent: emit })
    .catch((e) => emit({ type: "error", message: firstLine(e) }));
  return { id: live.id };
}

// Worked examples offered on the home page: a hunt per shipped tool, and scans of the demo repository in this repository.
const DEMO_REPO = process.env.FIXHUNT_DEMO_REPO ?? "https://github.com/and2049/fixhunt";
function examples(): HuntPageData["examples"] {
  const hunts = [["ruff", "FURB103"], ["biome", "complexity/noUselessLoneBlockStatements"], ["eslint", "prefer-const"], ["clang-tidy", "readability-container-size-empty"]].filter(([t]) => TOOLS[t]);
  const scans: Array<[string, string, string]> = [
    ["ruff", "cd python && python3 -m unittest discover -s tests -t .", "FURB103,FURB129,RUF019,PLR1733,UP015,UP004,F541,I001"],
    ["biome", "cd web && node --test", "style/useNumberNamespace,style/noUselessElse,complexity/noUselessLoneBlockStatements,style/noNegationElse,style/useConst"],
    ["eslint", "cd web && node --test", "prefer-const,no-var,object-shorthand,prefer-template,no-else-return"],
    ["clang-tidy", "make -s -C native test", "readability-container-size-empty,modernize-use-nullptr,readability-redundant-string-cstr"],
  ];
  return {
    hunts: hunts.map(([tool, rule]) => ({ tool, rule })),
    scans: scans.filter(([t]) => scanTools().includes(t)).map(([tool, run, rules]) => ({ tool, repo: DEMO_REPO, path: "demo/repo", run, rules })),
  };
}

function startScan(body: { tool: string; repo: string; path?: string; run: string; rules?: string; limit?: number; unsafe?: boolean }, code: string | undefined): { id: string } | { error: string } {
  const tool = TOOLS[body.tool];
  if (!tool || !scanTools().includes(body.tool)) return { error: `tool ${body.tool} is not available for scans` };
  const repo = parseRepoUrl(String(body.repo ?? ""));
  if (!repo) return { error: "repository must be an https URL on github.com, gitlab.com, codeberg.org or bitbucket.org" };
  const run = String(body.run ?? "").trim();
  if (!run || run.length > 400) return { error: "command required (at most 400 characters)" };
  const relPath = String(body.path ?? "").trim();
  if (relPath.length > 200 || /[\0]/.test(relPath)) return { error: "path must be a relative directory inside the repository" };
  const rules = String(body.rules ?? "").split(",").map((s) => s.trim()).filter(Boolean);
  if (rules.some((r) => !/^[\w.:/-]+$/.test(r) || r.split("/").some((s) => s === "" || /^\.+$/.test(s)))) return { error: "rules must be ids separated by commas" };
  if (!rules.length && !body.unsafe && !sweepCount(tool)) return { error: `${tool.id} labels no fix as safe: give rule ids, or tick unsafe fixes to try every rule` };
  const gate = allow(code, SCAN_ESTIMATE);
  if (!gate.ok) return { error: gate.reason };
  if (running && !running.done) return { error: `a ${running.kind} is already running; wait for it to finish` };
  const live = newJob("scan");
  const emit = emitter(live, () => { const d = live.events.find((e) => e.type === "done") as Extract<ScanEvent, { type: "done" }> | undefined; charge(gate.access.code, Math.max(SCAN_ESTIMATE, (d?.cost ?? 0) + 0.02)); });
  (async () => {
    emit({ type: "clone", url: repo.url, done: false });
    const c = await cloneRepo(repo.url);
    emit({ type: "clone", url: c.url, done: true, mb: c.mb, head: c.head });
    try {
      const sub = subdir(c.dir, relPath);
      if ("error" in sub) throw new Error(sub.error);
      await scan({ tool: tool as SpecTool, dir: sub.dir, path: sub.path || undefined, configRoot: c.dir, run, rules: rules.length ? rules : undefined, limit: Math.max(1, Math.min(SCAN_LIMIT, Number(body.limit) || SCAN_LIMIT)), unsafe: !!body.unsafe, timeoutMs: SCAN_TIMEOUT_MS, source: c.url, commit: c.head, quiet: true, onEvent: emit });
    } finally { removeClone(c.dir); }
  })().catch((e) => emit({ type: "error", message: firstLine(e) }));
  return { id: live.id };
}

function sse(live: Live): Response {
  const stream = new ReadableStream({
    start(ctrl) {
      const enc = new TextEncoder();
      const send = (e: JobEvent) => { try { ctrl.enqueue(enc.encode(`data: ${JSON.stringify(e)}\n\n`)); } catch { /* closed */ } };
      for (const e of live.events) send(e);
      if (live.done) { ctrl.close(); return; }
      const l = (e: JobEvent) => { send(e); if (e.type === "done" || e.type === "error") { live.listeners.delete(l); try { ctrl.close(); } catch { /* */ } } };
      live.listeners.add(l);
      const ka = setInterval(() => { try { ctrl.enqueue(enc.encode(": keepalive\n\n")); } catch { clearInterval(ka); } }, 15_000);
    },
  });
  return new Response(stream, { headers: { "content-type": "text/event-stream", "cache-control": "no-cache", connection: "keep-alive" } });
}

/** Read-only access to regular files under one root; the real path must stay inside the root (no symlink escapes). */
function serveFile(root: string, rel: string): Response {
  try {
    const rootReal = realpathSync(resolve(root));
    const p = realpathSync(resolve(root, rel));
    if (p !== rootReal && !p.startsWith(rootReal + sep)) return new Response("not found", { status: 404 });
    if (!statSync(p).isFile()) return new Response("not found", { status: 404 });
    const type = p.endsWith(".md") ? "text/markdown; charset=utf-8" : p.endsWith(".json") ? "application/json" : "text/plain; charset=utf-8";
    return new Response(readFileSync(p), { headers: { "content-type": type } });
  } catch { return new Response("not found", { status: 404 }); }
}

/** POST guard: same-origin (when a browser sends Origin) and the optional bearer token. */
function denyPost(req: Request, url: URL): Response | undefined {
  // Compare hosts, not schemes: behind a TLS-terminating proxy the server sees http:// while browsers send an https:// Origin
  const origin = req.headers.get("origin");
  let originHost: string | undefined;
  try { originHost = origin ? new URL(origin).host : undefined; } catch { originHost = "invalid"; }
  if (originHost && originHost !== url.host && originHost !== (req.headers.get("x-forwarded-host") ?? "")) return json({ error: "cross-origin request refused" }, 403);
  if (TOKEN) {
    const auth = req.headers.get("authorization") ?? "";
    if (auth !== `Bearer ${TOKEN}`) return json({ error: "token required" }, 401);
  }
  return undefined;
}

export function startServer(port: number, tools: Record<string, Tool>, hostname = process.env.FIXHUNT_HOST ?? "127.0.0.1") {
  TOOLS = tools;
  const server = Bun.serve({
    port,
    hostname,
    idleTimeout: 120,
    async fetch(req) {
      const url = new URL(req.url);
      const path = decodeURIComponent(url.pathname);
      try {
        if (path === "/") {
          const runs = loadRuns(); const fs = findings(runs);
          return html(huntPage({ catalog: catalogRules(Object.keys(TOOLS)), toolIds: Object.keys(TOOLS), scanTools: scanTools(), sweep: Object.fromEntries(scanTools().map((id) => [id, sweepCount(TOOLS[id])])), busy: running && !running.done ? { id: running.id, kind: running.kind } : undefined, gated: gated(), findings: fs, limits: { maxN: MAX_N, maxRounds: MAX_ROUNDS, scanLimit: SCAN_LIMIT }, examples: examples() }, L));
        }
        if (path === "/hunt") return redirect("/");
        if (path === "/about") return redirect("/docs");
        if (path === "/findings") { const runs = loadRuns(); const fs = findings(runs); return html(findingsPage(stats(runs, fs), fs, L)); }
        if (path === "/runs") { const runs = loadRuns(); return html(runsPage(runs, findings(runs), L)); }
        if (path === "/docs") { const runs = loadRuns(); return html(docsPage(stats(runs), spend(), L)); }
        if (path === "/scans") return html(scansPage(loadScans(), L));
        let m = /^\/s\/([^/]+)\/(accepted\.patch|reports\/[\w.-]+\.md|rules\/[\w.-]+\/minimal\.patch|scan\.md)$/.exec(path);
        if (m) return serveFile(RUNS_DIR, join(m[1], m[2]));
        m = /^\/s\/([^/]+)$/.exec(path);
        if (m) { const s = loadScans().find((x) => x.id === m![1]); if (!s) return html("scan not found", 404); return html(scanPage(s, s.findings.map((f) => ({ row: f, finding: scanFinding(s.id, f.rule) })).filter((x) => x.finding), L)); }
        m = /^\/r\/([^/]+)$/.exec(path);
        if (m) { const run = loadRuns().find((r) => r.id === m![1]); return run ? html(runPage(run, findings(), L)) : html("run not found", 404); }
        m = /^\/f\/([^/]+)\/([^/]+)$/.exec(path);
        if (m) { const f = findingByPath(m[1], m[2]); return f ? html(findingPage(f, L)) : html("finding not found", 404); }
        m = /^\/f\/([^/]+)\/([^/]+)\/fixture$/.exec(path);
        if (m) {
          const f = findingByPath(m[1], m[2]);
          if (!f) return html("finding not found", 404);
          return new Response(fixtureText(f), { headers: { "content-type": "text/plain; charset=utf-8", "content-disposition": `attachment; filename="${fixtureName(f)}"` } });
        }
        m = /^\/raw\/([^/]+)\/reports\/([^/]+\.(md|js|py|cpp))$/.exec(path);
        if (m) return serveFile(RUNS_DIR, join(m[1], "reports", m[2]));
        if (req.method === "POST") { const d = denyPost(req, url); if (d) return d; }
        if (path === "/api/hunt" && req.method === "POST") return json(startHunt(await req.json(), codeOf(req)));
        if (path === "/api/scan" && req.method === "POST") return json(startScan(await req.json(), codeOf(req)));
        if (path === "/api/access" && req.method === "POST") {
          const { code } = (await req.json()) as { code?: string };
          const a = lookup(code);
          if (!a) return json({ error: "unknown access code" }, 403);
          const r = remaining(a.code);
          return new Response(JSON.stringify({ ok: true, remaining: r.code, global: r.global, daily: a.daily }), { headers: { "content-type": "application/json", "set-cookie": `fixhunt_code=${encodeURIComponent(a.code)}; Path=/; HttpOnly; SameSite=Strict; Max-Age=2592000` } });
        }
        if (path === "/api/access") { const a = lookup(codeOf(req)); const r = a ? remaining(a.code) : { code: 0, global: remaining("").global }; return json({ gated: gated(), ok: !!a, remaining: r.code, global: r.global, daily: a?.daily ?? 0 }); }
        m = /^\/api\/(?:jobs|hunt)\/([^/]+)\/events$/.exec(path);
        if (m) { const live = jobs.get(m[1]); return live ? sse(live) : json({ error: "unknown job" }, 404); }
        m = /^\/api\/(?:jobs|hunt)\/([^/]+)$/.exec(path);
        if (m) { const live = jobs.get(m[1]); return live ? json({ id: live.id, kind: live.kind, done: live.done, events: live.events }) : json({ error: "unknown job" }, 404); }
        m = /^\/api\/rerun\/([^/]+)\/([^/]+)$/.exec(path);
        if (m && req.method === "POST") {
          const f = findingByPath(m[1], m[2]);
          if (!f) return json({ error: "finding not found" }, 404);
          const tool = TOOLS[f.run.tool];
          if (!tool) return json({ error: `tool ${f.run.tool} is not loaded` }, 400);
          if (rerunsInFlight >= MAX_RERUNS) return json({ error: "too many re-runs in flight; try again in a moment" }, 429);
          const gate = allow(codeOf(req), RERUN_ESTIMATE);
          if (!gate.ok) return json({ error: gate.reason }, 402);
          rerunsInFlight++;
          const dir = mkdtempSync(join(tmpdir(), "fixhunt-rerun-"));
          const t0 = Date.now();
          try {
            const r = await evaluateProgram(tool, f.run.rule, dir, { id: "rerun", title: "rerun", hazard: "", code: f.report.minimized, expectTrigger: true }, { unsafe: f.run.opts?.unsafe ?? false });
            const found = r.findings.find((x) => x.kind === f.report.kind);
            return json({ sandbox: await sandboxInfo(), ms: Date.now() - t0, version: await tool.version(), reproduced: !!found, error: r.error, before: r.before.run, after: r.after?.run, diff: r.after?.diff, findings: r.findings.map((x) => x.kind) });
          } finally {
            charge(gate.access.code, RERUN_ESTIMATE);
            rerunsInFlight--;
            rmSync(dir, { recursive: true, force: true });
          }
        }
        if (path === "/api/stats") { const runs = loadRuns(); return json(stats(runs)); }
        if (path === "/healthz") return new Response("ok");
        return html("not found", 404);
      } catch (e) {
        console.error(e);
        return html(`<pre>${String(e)}</pre>`, 500);
      }
    },
  });
  console.log(`fixhunt dashboard: http://${hostname}:${server.port}/${TOKEN ? " (POST endpoints need the token)" : ""}`);
  return server;
}
