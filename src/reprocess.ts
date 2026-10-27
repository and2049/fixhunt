// Re-run the finding pipeline (minimize → judge → dedup → evidence sheet) on finished runs,
// e.g. after the pipeline changed or when a sweep ran with an older build.
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { RUNS_DIR } from "./config";
import { evaluateProgram } from "./oracles";
import { writeJsonAtomic } from "./hunt";
import { evidenceOf, processFindings } from "./pipeline";
import type { Tool } from "./tools/types";

function runDirs(only?: string) {
  return readdirSync(RUNS_DIR).filter((d) => existsSync(join(RUNS_DIR, d, "results.json")) && (!only || d.includes(only))).sort();
}

export async function reprocess(tools: Record<string, Tool>, opts: { only?: string; force?: boolean }) {
  for (const d of runDirs(opts.only)) {
    const dir = join(RUNS_DIR, d);
    const run = JSON.parse(readFileSync(join(dir, "results.json"), "utf8"));
    const tool = tools[run.tool];
    if (!tool) continue;
    const hits = run.results.filter((r: any) => r.findings.some((f: any) => f.kind !== "disputed"));
    if (!hits.length) continue;
    const judged = (run.reports ?? []).filter((r: any) => r.verdict).length;
    if (!opts.force && judged === hits.length) continue;
    console.log(`${d}: ${hits.length} finding(s), ${judged} judged`);
    const pf = await processFindings(tool, run.rule, run.version, dir, run.results, run.opts?.unsafe ?? false, run.reports ?? []);
    run.reports = pf.reports;
    run.cost = (run.cost ?? 0) + pf.cost;
    writeJsonAtomic(join(dir, "results.json"), run);
  }
}

/** Model-free: fill in `evidence` for reports that predate it, by evaluating the minimized program once. */
export async function refreshEvidence(tools: Record<string, Tool>, opts: { only?: string; force?: boolean }) {
  let n = 0;
  for (const d of runDirs(opts.only)) {
    const dir = join(RUNS_DIR, d);
    const run = JSON.parse(readFileSync(join(dir, "results.json"), "utf8"));
    const tool = tools[run.tool];
    if (!tool || !run.reports?.length) continue;
    let changed = false;
    for (const rep of run.reports) {
      if (rep.evidence && !opts.force) continue;
      const unsafe = run.opts?.unsafe ?? false;
      const r = await evaluateProgram(tool, run.rule, join(dir, rep.programId, "min"), { id: `${rep.programId}-ev`, title: "min", hazard: "", code: rep.minimized, expectTrigger: true }, { unsafe });
      const f = r.findings.find((x) => x.kind === rep.kind);
      const md = existsSync(rep.reportPath) ? readFileSync(rep.reportPath, "utf8") : "";
      const ex = /## Why the rewrite is not equivalent[^\n]*\n\n([\s\S]*?)\n\n## /.exec(md)?.[1]?.trim();
      rep.evidence = evidenceOf(tool, run.rule, join(dir, rep.programId, "min", r.id), r, f?.detail ?? r.error ?? "(finding did not reproduce)", ex, unsafe);
      if (!f && r.error) {
        // The evaluation itself failed (sandbox outage, timeout): keep the finding, mark the evidence unconfirmed
        console.log(`  ${d} ${rep.programId}: evaluation failed on refresh (${r.error.split("\n")[0].slice(0, 80)}); kept, marked unconfirmed`);
        rep.evidence = { ...rep.evidence, confirmed: false };
        changed = true; n++;
        continue;
      }
      if (!f) {
        // The program ran and the finding is gone (e.g. better output normalization). Drop it from the run.
        console.log(`  ${d} ${rep.programId}: finding ${rep.kind} did not reproduce on refresh; dropped`);
        run.reports = run.reports.filter((x: any) => x !== rep);
        const res = run.results.find((x: any) => x.id === rep.programId);
        if (res) res.findings = res.findings.filter((x: any) => x.kind !== rep.kind);
      }
      changed = true; n++;
    }
    if (changed) writeJsonAtomic(join(dir, "results.json"), run);
  }
  console.log(`refreshed evidence for ${n} finding(s)`);
}
