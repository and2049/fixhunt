import { mkdirSync, renameSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { RUNS_DIR } from "./config";
import { analyzeRule, generatePrograms, screenProgram, type Feedback } from "./gen";
import { evaluateProgram, type ProgramResult } from "./oracles";
import { sandboxInfo } from "./sandbox";
import { processFindings, type FindingReport } from "./pipeline";
import type { Tool } from "./tools/types";

export type HuntOpts = { tool: Tool; rule: string; n: number; rounds: number; unsafe: boolean; seed?: number; model?: string; report?: boolean; onEvent?: (e: HuntEvent) => void; quiet?: boolean; parallel?: number };

/** Progress events, consumed by the CLI printer and by the dashboard's live feed. */
export type HuntEvent =
  | { type: "start"; runId: string; tool: string; version: string; rule: string; fixKind: string; sandbox: string }
  | { type: "analysis"; summary: string; fixDescription: string; hazards: string[]; firingShapes: number; cost: number }
  | { type: "round"; round: number; programs: number; cost: number }
  | { type: "round-failed"; round: number; error: string }
  | { type: "program"; id: string; title: string; hazard: string; status: "rejected" | "invalid" | "finding" | "silent" | "fix-ok" | "fired-no-fix"; detail: string; kinds: string[]; code?: string; diff?: string }
  | { type: "log"; message: string }
  | { type: "report"; programId: string; kind: string; grade?: string; severity?: string; lines: { before: number; after: number }; duplicates: Array<{ url: string; relation: string }> }
  | { type: "done"; runId: string; summary: Record<string, number>; cost: number; findings: number }
  | { type: "error"; message: string };


export async function hunt(o: HuntOpts) {
  const emit = (e: HuntEvent) => { o.onEvent?.(e); if (!o.quiet) printEvent(e); };
  const info = await o.tool.ruleInfo(o.rule);
  const version = await o.tool.version();
  const runId = `${new Date().toISOString().replace(/[:.]/g, "-")}-${Math.random().toString(36).slice(2, 6)}-${o.tool.id.replace(/[^\w.-]+/g, "_")}-${info.rule.replace(/[^\w.-]+/g, "_")}`;
  const dir = join(RUNS_DIR, runId);
  mkdirSync(dir, { recursive: true });
  emit({ type: "start", runId, tool: o.tool.id, version, rule: info.rule, fixKind: info.fixKind, sandbox: await sandboxInfo() });

  let cost = 0;
  const an = await analyzeRule(info, o.tool.language);
  cost += an.cost;
  writeFileSync(join(dir, "analysis.json"), JSON.stringify(an.analysis, null, 2));
  emit({ type: "analysis", summary: an.analysis.summary, fixDescription: an.analysis.fixDescription, hazards: an.analysis.hazards, firingShapes: an.analysis.firingShapes.length, cost: an.cost });

  const results: ProgramResult[] = [];
  const seen = new Set<string>();
  let feedback: Feedback | undefined;
  for (let round = 0; round < o.rounds; round++) {
    let gen;
    try {
      gen = await generatePrograms(info, an.analysis, { n: o.n, language: o.tool.language, runner: o.tool.runnerHint ?? "", seed: (o.seed ?? 1) * 7919 + round, feedback, model: o.model });
    } catch (e) {
      emit({ type: "round-failed", round: round + 1, error: String(e).split("\n")[0].slice(0, 160) });
      continue;
    }
    cost += gen.cost;
    emit({ type: "round", round: round + 1, programs: gen.programs.length, cost: gen.cost });
    const fb: Feedback = { silent: [], invalid: [], fixOk: [] };
    const todo: Array<{ p: typeof gen.programs[number]; pid: string }> = [];
    for (const p of gen.programs) {
      const key = p.code.replace(/\s+/g, " ").trim();
      if (seen.has(key)) continue;
      seen.add(key);
      const pid = `r${round + 1}-${p.id}`;
      const why = screenProgram(o.tool.language, p.code);
      if (why) { emit({ type: "program", id: pid, title: p.title, hazard: p.hazard, status: "rejected", detail: why, kinds: [], code: p.code }); fb.invalid.push(`${p.title}: ${why}`); continue; }
      todo.push({ p, pid });
    }
    const evaluated = await mapLimit(todo, o.parallel ?? Number(process.env.FIXHUNT_PARALLEL ?? 6), async ({ p, pid }) => ({ p, r: await evaluateProgram(o.tool, info, dir, { ...p, id: pid }, { unsafe: o.unsafe }) }));
    for (const { p, r } of evaluated) {
      const pid = r.id;
      results.push(r);
      const desc = `${p.title} (${p.hazard.slice(0, 80)})`;
      const kinds = r.findings.map((f) => f.kind);
      let status: Extract<HuntEvent, { type: "program" }>["status"];
      let detail: string;
      if (r.error) { status = "invalid"; detail = r.error.split("\n")[0].slice(0, 120); fb.invalid.push(desc); }
      else if (kinds.some((k) => k !== "disputed")) { status = "finding"; detail = r.findings.find((f) => f.kind !== "disputed")!.detail; }
      else if (!r.before.diagnostics.length) { status = "silent"; detail = p.expectTrigger ? "expected to fire" : "as predicted"; if (p.expectTrigger) fb.silent.push(desc); }
      else if (r.after?.changed) { status = "fix-ok"; detail = "fix applied, behavior unchanged"; fb.fixOk.push(desc); }
      else { status = "fired-no-fix"; detail = "rule fired, no fix offered"; }
      emit({ type: "program", id: pid, title: r.title, hazard: r.hazard, status, detail, kinds, code: p.code, diff: r.after?.diff });
    }
    feedback = fb;
  }
  let reports: FindingReport[] = [];
  if (o.report !== false) {
    const pf = await processFindings(o.tool, info, version, dir, results, o.unsafe, [], (message) => emit({ type: "log", message }), (r) => emit({ type: "report", programId: r.programId, kind: r.kind, grade: r.verdict?.grade, severity: r.verdict?.severity, lines: r.lines, duplicates: r.duplicates }));
    reports = pf.reports;
    cost += pf.cost;
  }
  const summary = summarize(results);
  writeJsonAtomic(join(dir, "results.json"), { runId, tool: o.tool.id, ext: o.tool.ext, version, rule: info, analysis: an.analysis, opts: { n: o.n, rounds: o.rounds, unsafe: o.unsafe, model: o.model }, cost, summary, reports, results });
  emit({ type: "done", runId, summary, cost, findings: results.filter((r) => r.findings.some((f) => f.kind !== "disputed")).length });
  return { dir, runId, results, summary, reports, cost };
}

/** Write JSON to a temp file and rename, so readers never see a partial file. */
export function writeJsonAtomic(file: string, value: unknown) {
  const tmp = `${file}.${process.pid}.tmp`;
  writeFileSync(tmp, JSON.stringify(value, null, 2));
  renameSync(tmp, file);
}

/** Run `fn` over `items` with at most `limit` in flight; results keep input order. */
async function mapLimit<T, R>(items: T[], limit: number, fn: (t: T) => Promise<R>): Promise<R[]> {
  const out: R[] = new Array(items.length);
  let next = 0;
  const worker = async () => { for (;;) { const i = next++; if (i >= items.length) return; out[i] = await fn(items[i]); } };
  await Promise.all(Array.from({ length: Math.max(1, Math.min(limit, items.length)) }, worker));
  return out;
}

function printEvent(e: HuntEvent) {
  switch (e.type) {
    case "start": return console.log(`hunt ${e.runId}\n  ${e.tool} ${e.version}, rule ${e.rule} (fix: ${e.fixKind}), sandbox: ${e.sandbox}`);
    case "analysis": return console.log(`  analysis: ${e.hazards.length} rule-specific hazards, ${e.firingShapes} firing shapes ($${e.cost.toFixed(4)})`);
    case "round": return console.log(`  round ${e.round}: ${e.programs} programs ($${e.cost.toFixed(4)})`);
    case "round-failed": return console.log(`  round ${e.round}: generation failed (${e.error}); skipping round`);
    case "program": return console.log(`    ${e.id} ${e.status === "finding" ? e.kinds.join(",") : e.status === "rejected" || e.status === "invalid" ? `${e.status} (${e.detail.slice(0, 60)})` : e.status}  — ${e.title}`);
    case "log": return console.log(`  ${e.message}`);
    case "report": return console.log(`    ${e.programId} ${e.kind}: ${e.lines.before}→${e.lines.after} lines; judge: ${e.grade ? `${e.grade}/${e.severity}` : "n/a"}; ${e.duplicates.length ? e.duplicates.map((d) => `${d.relation} ${d.url}`).join(", ") : "no upstream match"}`);
    case "done": return console.log(`\n${JSON.stringify(e.summary)}\n  model cost $${e.cost.toFixed(4)}; artifacts in ${RUNS_DIR}/${e.runId}`);
    case "error": return console.log(`  error: ${e.message}`);
  }
}

function summarize(rs: ProgramResult[]) {
  const s: Record<string, number> = { programs: rs.length, invalid: 0, fired: 0, fixed: 0 };
  for (const r of rs) {
    if (r.error) s.invalid++;
    if (r.before.diagnostics.length) s.fired++;
    if (r.after?.changed) s.fixed++;
    for (const f of r.findings) s[f.kind] = (s[f.kind] ?? 0) + 1;
  }
  return s;
}
