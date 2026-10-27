// Read model for the dashboard: runs, ranked findings and spend. Pure file reads, cached by mtime.
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import { RUNS_DIR } from "../config";
import type { FindingReport } from "../pipeline";
import type { ProgramResult } from "../oracles";
import type { RuleInfo } from "../tools/types";

export type Run = {
  id: string; dir: string; tool: string; ext: string; version: string; rule: RuleInfo; analysis?: any;
  opts?: { n: number; rounds: number; unsafe: boolean; model?: string }; cost: number; summary: Record<string, number>;
  reports: FindingReport[]; results: ProgramResult[]; when: string;
};

export type Finding = {
  run: Run; report: FindingReport; result: ProgramResult; grade: string; severity: string; upstream: "duplicate" | "related" | "none"; rank: number;
};

const GRADE_ORDER: Record<string, number> = { real: 0, unclear: 1, unjudged: 2, "intended-change": 3, "introspection-only": 4, "program-bug": 5 };
const SEV_ORDER: Record<string, number> = { high: 0, medium: 1, low: 2, "-": 3 };

let cache: { key: string; runs: Run[] } | undefined;

function runKey(): string {
  if (!existsSync(RUNS_DIR)) return "";
  return readdirSync(RUNS_DIR).map((d) => { const f = join(RUNS_DIR, d, "results.json"); return existsSync(f) ? `${d}:${statSync(f).mtimeMs}` : ""; }).join("|");
}

export function loadRuns(): Run[] {
  const key = runKey();
  if (cache && cache.key === key) return cache.runs;
  const runs: Run[] = [];
  if (existsSync(RUNS_DIR)) for (const d of readdirSync(RUNS_DIR)) {
    const f = join(RUNS_DIR, d, "results.json");
    if (!existsSync(f)) continue;
    try {
      const j = JSON.parse(readFileSync(f, "utf8"));
      const when = d.slice(0, 24).replace(/^(\d{4}-\d\d-\d\d)T(\d\d)-(\d\d)-(\d\d)-(\d{3})Z$/, "$1T$2:$3:$4.$5Z");
      runs.push({ id: d, dir: join(RUNS_DIR, d), tool: j.tool, ext: j.ext ?? extOf(join(RUNS_DIR, d)), version: j.version, rule: j.rule, analysis: j.analysis, opts: j.opts, cost: j.cost ?? 0, summary: j.summary ?? {}, reports: j.reports ?? [], results: j.results ?? [], when });
    } catch { /* partial write in progress */ }
  }
  runs.sort((a, b) => b.id.localeCompare(a.id));
  cache = { key, runs };
  return runs;
}

/** Older runs did not record the file extension; read it from the first program's original source file. */
function extOf(dir: string): string {
  try {
    for (const p of readdirSync(dir)) { try { const f = readdirSync(join(dir, p)).find((n) => n.startsWith("orig.")); if (f) return f.slice(5); } catch { /* a file, not a program directory */ } }
  } catch { /* fall through */ }
  return "txt";
}

export function findings(runs = loadRuns()): Finding[] {
  const out: Finding[] = [];
  for (const run of runs) for (const report of run.reports) {
    const result = run.results.find((r) => r.id === report.programId);
    if (!result) continue;
    const rel = report.duplicates.map((d) => d.relation);
    out.push({ run, report, result, grade: report.verdict?.grade ?? "unjudged", severity: report.verdict?.severity ?? "-", upstream: rel.includes("duplicate") ? "duplicate" : rel.includes("related") ? "related" : "none", rank: 0 });
  }
  out.sort((a, b) => (GRADE_ORDER[a.grade] ?? 9) - (GRADE_ORDER[b.grade] ?? 9) || (SEV_ORDER[a.severity] ?? 9) - (SEV_ORDER[b.severity] ?? 9) || Number(b.report.safeLabel) - Number(a.report.safeLabel) || a.run.rule.rule.localeCompare(b.run.rule.rule) || a.run.id.localeCompare(b.run.id));
  out.forEach((f, i) => (f.rank = i + 1));
  return out;
}

export function countByRun(fs: Finding[]): Map<string, number> {
  const m = new Map<string, number>();
  for (const f of fs) m.set(f.run.id, (m.get(f.run.id) ?? 0) + 1);
  return m;
}

export function findingByPath(runId: string, pid: string): Finding | undefined {
  return findings().find((f) => f.run.id === runId && f.report.programId === pid);
}

export type ScanUpstream = { queries: string[]; duplicates: Array<{ url: string; relation: string }>; fixedIn?: string; fixedUrl?: string; bank?: { runId: string; programId: string; grade: string; findings: number }; cost: number };
export type ScanRisk = { file?: string; enabled?: number; note?: string; known: Array<{ rule: string; fixKind: string; findings: number; confirmed?: number; safe: number; grade: string; severity: string; status?: string; issue?: string; urls: Array<{ url: string; relation: string }>; runId: string; programId: string }>; notEnabled: number };
export type ScanLint = { before: number; after: number; files: number; skipped?: number; sample: string[]; note?: string; label?: string };
export type ScanFindingRow = { rule: string; kind: string; changedFiles: string[]; exitBefore: number | null; exitAfter: number | null; lint?: ScanLint; minimal?: { hunks: number; of: number; files: string[]; complete?: boolean; confirmed: boolean; note?: string }; verdict?: { grade: string; severity: string }; upstream?: ScanUpstream; report?: string };
export type Scan = {
  id: string; dir: string; tool: string; version: string; project: string; commit?: string; path?: string; run: string; rules: number; applied: number; cost: number;
  findings: ScanFindingRow[]; incomplete: Array<{ rule: string } & ScanLint>; when: string;
  risk?: ScanRisk; accepted?: string[]; combined?: { rules: string[]; files: number; verified: boolean; exitBefore: number | null; exitAfter: number | null; timedOut: boolean; note?: string; patch?: boolean }; errors: string[]; warnings: string[];
};

export function loadScans(): Scan[] {
  const out: Scan[] = [];
  if (!existsSync(RUNS_DIR)) return out;
  for (const d of readdirSync(RUNS_DIR)) {
    const f = join(RUNS_DIR, d, "scan.json");
    if (!existsSync(f)) continue;
    try {
      const j = JSON.parse(readFileSync(f, "utf8"));
      out.push({ id: d, dir: join(RUNS_DIR, d), tool: j.tool, version: j.version, project: j.dir, commit: j.commit, path: typeof j.path === "string" ? j.path : undefined, run: j.run, rules: j.rules, applied: j.applied, cost: j.cost ?? 0, findings: j.findings ?? [], incomplete: Array.isArray(j.incomplete) ? j.incomplete : [], risk: j.risk, accepted: j.accepted, combined: j.combined, errors: Array.isArray(j.errors) ? j.errors.map(String) : [], warnings: Array.isArray(j.warnings) ? j.warnings.map(String) : [], when: d.slice(0, 24).replace(/^(\d{4}-\d\d-\d\d)T(\d\d)-(\d\d)-(\d\d)-(\d{3})Z$/, "$1T$2:$3:$4.$5Z") });
    } catch { /* partial */ }
  }
  return out.sort((a, b) => b.id.localeCompare(a.id));
}

export function scanFinding(scanId: string, rule: string): any | undefined {
  const f = join(RUNS_DIR, scanId, "rules", rule.replace(/[^\w.-]+/g, "_"), "finding.json");
  try { return JSON.parse(readFileSync(f, "utf8")); } catch { return undefined; }
}

export type Spend = { total: number; byModel: Record<string, { calls: number; cost: number; prompt: number; completion: number }>; byTag: Record<string, { calls: number; cost: number }> };

export function spend(): Spend {
  const s: Spend = { total: 0, byModel: {}, byTag: {} };
  const f = join(RUNS_DIR, "spend.jsonl");
  if (!existsSync(f)) return s;
  for (const line of readFileSync(f, "utf8").split("\n")) {
    if (!line.trim()) continue;
    try {
      const j = JSON.parse(line);
      s.total += j.cost ?? 0;
      const m = (s.byModel[j.model] ??= { calls: 0, cost: 0, prompt: 0, completion: 0 });
      m.calls++; m.cost += j.cost ?? 0; m.prompt += j.prompt ?? 0; m.completion += j.completion ?? 0;
      const t = (s.byTag[j.tag ?? "?"] ??= { calls: 0, cost: 0 });
      t.calls++; t.cost += j.cost ?? 0;
    } catch { /* skip */ }
  }
  return s;
}

export type Stats = {
  runs: number; tools: string[]; rules: number; programs: number; fired: number; fixed: number; findings: number; safeFindings: number;
  grades: Record<string, number>; kinds: Record<string, number>; versions: Record<string, string>; cost: number;
  sandboxRuns: number; sandboxCost: number;
};

export function stats(runs = loadRuns(), fs = findings(runs)): Stats {
  const sp = spend();
  const st: Stats = { runs: runs.length, tools: [], rules: 0, programs: 0, fired: 0, fixed: 0, findings: fs.length, safeFindings: 0, grades: {}, kinds: {}, versions: {}, cost: 0, sandboxRuns: sp.byTag.sandbox?.calls ?? 0, sandboxCost: sp.byTag.sandbox?.cost ?? 0 };
  const rules = new Set<string>();
  for (const r of runs) {
    rules.add(`${r.tool} ${r.rule.rule}`);
    st.programs += r.summary.programs ?? 0; st.fired += r.summary.fired ?? 0; st.fixed += r.summary.fixed ?? 0; st.cost += r.cost;
    st.versions[r.tool] ??= r.version;
    if (!st.tools.includes(r.tool)) st.tools.push(r.tool);
  }
  st.rules = rules.size;
  for (const f of fs) {
    st.grades[f.grade] = (st.grades[f.grade] ?? 0) + 1;
    st.kinds[f.report.kind] = (st.kinds[f.report.kind] ?? 0) + 1;
    if (f.report.safeLabel) st.safeFindings++;
  }
  return st;
}

export function catalogRules(toolIds: string[]): Record<string, Array<{ rule: string; fixKind: string }>> {
  const out: Record<string, Array<{ rule: string; fixKind: string }>> = {};
  for (const t of toolIds) {
    try { const j = JSON.parse(readFileSync(`data/${t}-rules.json`, "utf8")); out[t] = (Array.isArray(j) ? j : j.rules).filter((r: any) => r.fixKind !== "none").map((r: any) => ({ rule: r.rule, fixKind: r.fixKind })); } catch { out[t] = []; }
  }
  return out;
}

const COMMENT: Record<string, string> = { py: "#", js: "//", cjs: "//", mjs: "//", ts: "//", cpp: "//", cc: "//", c: "//", rs: "//", go: "//" };
const oneLine = (t: string) => t.replace(/\s+/g, " ").trim();
const outLine = (s: { stdout: string; stderr1: string; code: number | null; timedOut: boolean }) => {
  const o = oneLine(s.stdout).slice(0, 200);
  return `${o ? `stdout "${o}"` : "no stdout"}${s.stderr1 ? `, stderr "${oneLine(s.stderr1).slice(0, 120)}"` : ""}, ${s.timedOut ? "timed out" : `exit ${s.code}`}`;
};
/** The minimized program as a regression fixture for the tool's own test suite: a comment header that states what the
 * fix did to it, then the program unchanged. */
export function fixtureText(f: Finding): string {
  const c = COMMENT[f.run.ext] ?? "//";
  const ev = f.report.evidence;
  const lines = [
    `fixhunt regression fixture: ${f.run.tool} ${f.run.rule.rule}, ${f.run.version}`,
    `${f.report.safeLabel ? "the fix labelled safe" : "the fix"} ${KIND_SENTENCE[f.report.kind] ?? f.report.kind} on this program`,
    ...(ev ? [`before the fix: ${outLine(ev.before)}`, ...(ev.after ? [`after the fix: ${outLine(ev.after)}`] : [])] : []),
    `finding ${f.run.id}/${f.report.programId}; rule fired ${ev?.fired ?? "?"} time(s) before the fix`,
  ];
  const program = f.report.minimized.replace(/\s+$/, "") + "\n";
  const header = lines.map((l) => `${c} ${l}`).join("\n") + "\n\n";
  // A hashbang must stay on the first line
  const hb = /^#![^\n]*\n/.exec(program);
  return hb ? hb[0] + header + program.slice(hb[0].length) : header + program;
}
export function fixtureName(f: Finding): string {
  const rule = f.run.rule.rule.replace(/[^\w.-]+/g, "-");
  return `${f.run.tool}-${rule}-${f.report.programId}.${f.run.ext}`.replace(/[^\w.-]/g, "-");
}
const KIND_SENTENCE: Record<string, string> = {
  "fix-changes-behavior": "changes the program's output",
  "fix-breaks-syntax": "produces a program that does not parse",
  "fix-not-fixpoint": "is not a fixpoint (the rule fires again on its own output)",
  "fix-introduces-diagnostic": "introduces new diagnostics of the same rule",
  "tool-crash": "crashed the tool",
};
