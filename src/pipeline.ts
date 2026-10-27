// Post-processing for oracle-backed findings: minimize → judge → dedup → evidence sheet.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { dedup, type DedupResult } from "./dedup";
import { judgeFinding, type Verdict } from "./judge";
import { minimize } from "./minimize";
import { evaluateProgram, type ProgramResult, type Snap } from "./oracles";
import { writeReport } from "./report";
import type { RuleInfo, Tool } from "./tools/types";

/** Everything the dashboard shows for one finding, computed from the minimized program. */
export type Evidence = { diff: string; observed: string; before: Snap; after?: Snap; fixed: string; commands: string[]; explanation?: string; fired: number; firedAfter: number; confirmed?: boolean };

export type FindingReport = { programId: string; kind: string; safeLabel: boolean; minimized: string; lines: { before: number; after: number }; reportPath: string; duplicates: Array<{ url: string; relation: string }>; verdict?: Verdict; dedup?: DedupResult; evidence?: Evidence; minimizer?: { evaluations: number; proposal?: string } };

export function evidenceOf(tool: Tool, info: RuleInfo, dir: string, r: ProgramResult, observed: string, explanation?: string, unsafe = false): Evidence {
  const fixedPath = join(dir, `fixed.${tool.ext}`);
  return {
    diff: r.after?.diff ?? "", observed, before: r.before.run, after: r.after?.run,
    fixed: existsSync(fixedPath) ? readFileSync(fixedPath, "utf8") : "",
    commands: tool.reproCommands(info.rule, `prog.${tool.ext}`, unsafe), explanation,
    fired: r.before.diagnostics.length, firedAfter: r.after?.diagnostics.length ?? 0,
  };
}

export async function processFindings(tool: Tool, info: RuleInfo, version: string, dir: string, results: ProgramResult[], unsafe: boolean, prior: FindingReport[] = [], log: (m: string) => void = (m) => console.log("  " + m), onReport?: (r: FindingReport) => void): Promise<{ reports: FindingReport[]; cost: number }> {
  const reports: FindingReport[] = [];
  let cost = 0;
  const hits = results.filter((r) => r.findings.some((f) => f.kind !== "disputed"));
  if (!hits.length) return { reports, cost };
  mkdirSync(join(dir, "reports"), { recursive: true });
  log(`${hits.length} oracle-backed finding(s): minimizing, searching upstream, writing evidence sheets`);
  for (const r of hits) {
    const f = r.findings.find((x) => x.kind !== "disputed")!;
    const prog = r.id;
    const src = readFileSync(join(dir, prog, `orig.${tool.ext}`), "utf8");
    const old = prior.find((p) => p.programId === prog);
    const minDir = join(dir, prog, "min");
    let m: { code: string; lines: { before: number; after: number }; evaluations: number; result: ProgramResult; proposal?: string; cost?: number };
    if (old?.minimized) {
      // Reuse the earlier minimization: evaluate the minimized program once to refresh the evidence
      const rr = await evaluateProgram(tool, info, minDir, { id: `${prog}-reuse`, title: "min", hazard: "", code: old.minimized, expectTrigger: true }, { unsafe });
      m = rr.findings.some((x) => x.kind === f.kind) ? { code: old.minimized, lines: old.lines, evaluations: 1, result: rr } : await minimize(tool, info, minDir, prog, src, f.kind, unsafe);
    } else {
      m = await minimize(tool, info, minDir, prog, src, f.kind, unsafe);
    }
    let confirmed: boolean | undefined;
    if (!old?.minimized) {
      // Confirm the minimized program in the real sandbox; evidence and judge input come from this run
      const conf = await evaluateProgram(tool, info, minDir, { id: `${prog}-confirm`, title: "min", hazard: "", code: m.code, expectTrigger: true }, { unsafe });
      confirmed = conf.findings.some((x) => x.kind === f.kind);
      if (confirmed) m = { ...m, result: conf };
      else log(`  ${prog}: minimized program did not reproduce in the sandbox (${conf.error ?? "no finding"}); reported as unconfirmed`);
    } else confirmed = true; // the reuse path above evaluated it in the current sandbox
    cost += m.cost ?? 0;
    const mf = m.result.findings.find((x) => x.kind === f.kind) ?? f;
    const diff = m.result.after?.diff ?? "";
    let verdict: Verdict | undefined;
    try {
      const j = await judgeFinding({ tool: tool.id, rule: info.rule, fixKind: info.fixKind, kind: f.kind, observed: mf.detail, repro: m.code, diff, docs: info.docs, before: m.result.before.run, after: m.result.after?.run });
      verdict = j.verdict;
      cost += j.cost;
    } catch (e) {
      log(`  judge failed: ${String(e).slice(0, 120)}`);
    }
    const dd = old?.dedup ?? (await dedup({ tool: tool.id, repo: tool.repo, rule: info.rule, kind: f.kind, observed: mf.detail, repro: m.code, diff }));
    if (!old?.dedup) cost += dd.cost;
    const file = `prog.${tool.ext}`;
    const rep = await writeReport({ tool: tool.id, version, info, finding: mf, result: m.result, minimized: { code: m.code, lines: m.lines }, dedup: dd, commands: tool.reproCommands(info.rule, file, unsafe), runner: "", verdict, fence: tool.docsFence ?? tool.language });
    cost += rep.cost;
    const reportPath = join(dir, "reports", `${prog}.md`);
    writeFileSync(reportPath, rep.markdown);
    writeFileSync(join(dir, "reports", `${prog}.${tool.ext}`), m.code);
    const duplicates = dd.verdicts.filter((v) => v.relation !== "unrelated").map((v) => ({ url: v.url, relation: v.relation }));
    const evidence = { ...evidenceOf(tool, info, join(minDir, m.result.id), m.result, mf.detail, rep.explanation, unsafe), confirmed };
    const out: FindingReport = { programId: prog, kind: f.kind, safeLabel: mf.safeLabel, minimized: m.code, lines: m.lines, reportPath, duplicates, verdict, dedup: dd, evidence, minimizer: old?.minimized ? old.minimizer : { evaluations: m.evaluations, proposal: m.proposal } };
    reports.push(out);
    onReport?.(out);
    if (!onReport) log(`  ${prog} ${f.kind}: ${m.lines.before}→${m.lines.after} lines in ${m.evaluations} evals; judge: ${verdict ? `${verdict.grade}/${verdict.severity}` : "n/a"}; ${duplicates.length ? duplicates.map((d) => `${d.relation} ${d.url}`).join(", ") : "no upstream match"} → ${reportPath}`);
  }
  return { reports, cost };
}
