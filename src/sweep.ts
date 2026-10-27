// Sweep: hunt every rule the tool spec's sweep section selects (by default, every rule with a fix labelled safe).
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { catalogFor, sweepRules, type CatalogRule } from "./catalog";
import { RUNS_DIR } from "./config";
import { hunt } from "./hunt";
import type { SpecTool } from "./tools/spec";

export type SweepOpts = { tool: SpecTool; n: number; rounds: number; unsafe: boolean; limit?: number; only?: RegExp; resume?: boolean };

export async function sweep(o: SweepOpts) {
  const catalog = await catalogFor(o.tool);
  let rules: CatalogRule[] = sweepRules(o.tool, catalog, o.unsafe);
  if (o.only) rules = rules.filter((r) => o.only!.test(r.rule));
  if (o.limit) rules = rules.slice(0, o.limit);
  const stateFile = join(RUNS_DIR, `sweep-${o.tool.id}.json`);
  const version = await o.tool.version();
  const state: Record<string, { dir: string; findings: number; summary: any; version?: string }> = o.resume && existsSync(stateFile) ? JSON.parse(readFileSync(stateFile, "utf8")) : {};
  mkdirSync(RUNS_DIR, { recursive: true });
  // Resume only what this tool version already finished; failed rules and other versions are retried
  const done = (r: CatalogRule) => state[r.rule] && state[r.rule].findings >= 0 && (state[r.rule].version ?? version) === version;
  console.log(`sweep ${o.tool.id} ${version}: ${rules.length} rules (${rules.filter(done).length} already done)`);
  let i = 0;
  for (const r of rules) {
    i++;
    if (done(r)) continue;
    console.log(`\n[${i}/${rules.length}] ${r.rule}`);
    try {
      const h = await hunt({ tool: o.tool, rule: r.rule, n: o.n, rounds: o.rounds, unsafe: o.unsafe, seed: i });
      const findings = h.results.filter((x) => x.findings.some((f) => f.kind !== "disputed")).length;
      state[r.rule] = { dir: h.dir, findings, summary: h.summary, version };
    } catch (e) {
      console.log(`  failed: ${String(e).split("\n")[0].slice(0, 160)}`);
      state[r.rule] = { dir: "", findings: -1, summary: { error: String(e).slice(0, 200) }, version };
    }
    writeFileSync(stateFile, JSON.stringify(state, null, 1));
  }
  const withFindings = Object.entries(state).filter(([, v]) => v.findings > 0);
  console.log(`\nsweep done: ${withFindings.length} rule(s) with oracle-backed findings:\n${withFindings.map(([k, v]) => `  ${k}: ${v.findings} (${v.dir})`).join("\n")}`);
}
