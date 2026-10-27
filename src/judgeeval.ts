// Judge evaluation against hand labels (data/judge-labels.json: "tool rule" -> expected grade).
// --stored scores the verdicts already in results.json (free); otherwise re-judges live with the current prompt.
import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { judgeFinding, type Verdict } from "./judge";
import { loadRuns } from "./web/data";

export async function judgeEval(opts: { stored: boolean; limit?: number; only?: string; out?: string }) {
  const labels: Record<string, string> = JSON.parse(readFileSync("data/judge-labels.json", "utf8"));
  const grades = ["real", "intended-change", "introspection-only", "program-bug", "unclear"];
  const matrix: Record<string, Record<string, number>> = {};
  const rows: Array<{ key: string; id: string; expected: string; got: string; why: string }> = [];
  let cost = 0, n = 0;
  const items: Array<{ run: ReturnType<typeof loadRuns>[number]; rep: any; key: string; expected: string }> = [];
  for (const run of loadRuns()) {
    const key = `${run.tool} ${run.rule.rule}`;
    const expected = labels[key];
    if (!expected || (opts.only && !key.includes(opts.only))) continue;
    for (const rep of run.reports) { if (opts.limit && items.length >= opts.limit) break; items.push({ run, rep, key, expected }); }
  }
  n = items.length;
  const verdicts: Array<Verdict | undefined> = new Array(n);
  let next = 0;
  const worker = async () => {
    for (;;) {
      const i = next++; if (i >= n) return;
      const { run, rep } = items[i];
      if (opts.stored) { verdicts[i] = rep.verdict; continue; }
      const ev = rep.evidence;
      try {
        const r = await judgeFinding({ tool: run.tool, rule: run.rule.rule, fixKind: run.rule.fixKind, kind: rep.kind, observed: ev?.observed ?? "", repro: rep.minimized, diff: ev?.diff ?? "", docs: run.rule.docs, before: ev?.before, after: ev?.after });
        verdicts[i] = r.verdict; cost += r.cost;
      } catch (e) { console.log(`judge failed for ${items[i].key} ${rep.programId}: ${String(e).slice(0, 100)}`); }
      const got = verdicts[i]?.grade ?? "unjudged";
      console.log(`${got === items[i].expected ? "ok " : "XX "} ${items[i].key} ${rep.programId}: expected ${items[i].expected}, got ${got}${verdicts[i]?.differenceSource ? ` (${verdicts[i]!.differenceSource})` : ""}`);
    }
  };
  await Promise.all(Array.from({ length: opts.stored ? 1 : 4 }, worker));
  for (let i = 0; i < n; i++) {
    const { key, rep, expected } = items[i];
    const got = verdicts[i]?.grade ?? "unjudged";
    (matrix[expected] ??= {})[got] = (matrix[expected]![got] ?? 0) + 1;
    rows.push({ key, id: rep.programId, expected, got, why: verdicts[i]?.why ?? "" });
  }
  const header = `expected \\ got`.padEnd(32) + grades.map((g) => g.padStart(19)).join("");
  console.log(header);
  let correct = 0;
  for (const e of Object.keys(matrix)) {
    console.log(e.padEnd(32) + grades.map((g) => String(matrix[e][g] ?? 0).padStart(19)).join(""));
    correct += matrix[e][e] ?? 0;
  }
  const realAsReal = matrix.real?.real ?? 0, realTotal = Object.values(matrix.real ?? {}).reduce((a, b) => a + b, 0);
  const notRealAsReal = Object.entries(matrix).filter(([e]) => e !== "real").reduce((a, [, m]) => a + (m.real ?? 0), 0);
  const gotReal = realAsReal + notRealAsReal;
  console.log(`\n${n} findings, accuracy ${(100 * correct / n).toFixed(0)}%, real recall ${realTotal ? (100 * realAsReal / realTotal).toFixed(0) : "-"}%, real precision ${gotReal ? (100 * realAsReal / gotReal).toFixed(0) : "-"}%, cost $${cost.toFixed(3)}`);
  if (opts.out) writeFileSync(opts.out, JSON.stringify({ matrix, rows }, null, 1));
}
