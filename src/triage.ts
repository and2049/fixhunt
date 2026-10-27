// Triage table across all runs: one row per oracle-backed finding, real-graded first.
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { RUNS_DIR } from "./config";

type Row = { tool: string; rule: string; run: string; id: string; kind: string; safe: boolean; grade: string; severity: string; why: string; dups: string[]; report: string };

export function triageRows(filterTool?: string): Row[] {
  const rows: Row[] = [];
  for (const d of readdirSync(RUNS_DIR)) {
    const f = join(RUNS_DIR, d, "results.json");
    if (!existsSync(f)) continue;
    const run = JSON.parse(readFileSync(f, "utf8"));
    if (filterTool && run.tool !== filterTool) continue;
    for (const rep of run.reports ?? []) {
      rows.push({
        tool: run.tool, rule: run.rule.rule, run: d, id: rep.programId, kind: rep.kind, safe: rep.safeLabel,
        grade: rep.verdict?.grade ?? "unjudged", severity: rep.verdict?.severity ?? "-", why: rep.verdict?.why ?? "",
        dups: (rep.duplicates ?? []).map((x: any) => `${x.relation} ${x.url.replace(/^https:\/\/github\.com\//, "")}`),
        report: rep.reportPath,
      });
    }
  }
  const order: Record<string, number> = { real: 0, unclear: 1, unjudged: 2, "intended-change": 3, "introspection-only": 4, "program-bug": 5 };
  const sev: Record<string, number> = { high: 0, medium: 1, low: 2, "-": 3 };
  rows.sort((a, b) => (order[a.grade] ?? 9) - (order[b.grade] ?? 9) || (sev[a.severity] ?? 9) - (sev[b.severity] ?? 9) || a.rule.localeCompare(b.rule));
  return rows;
}

export function triageMarkdown(filterTool?: string): string {
  const rows = triageRows(filterTool);
  const counts: Record<string, number> = {};
  for (const r of rows) counts[r.grade] = (counts[r.grade] ?? 0) + 1;
  const lines = [`# Triage (${rows.length} findings: ${Object.entries(counts).map(([k, v]) => `${v} ${k}`).join(", ")})`, ""];
  let current = "";
  for (const r of rows) {
    if (r.grade !== current) { current = r.grade; lines.push(`## ${current}`, ""); }
    lines.push(`- **${r.tool} ${r.rule}** ${r.id} · ${r.kind}${r.safe ? " · labelled safe" : ""} · severity ${r.severity}${r.dups.length ? " · " + r.dups.join(", ") : ""}`);
    if (r.why) lines.push(`  ${r.why}`);
    lines.push(`  [${r.report}](../${r.report})`);
  }
  return lines.join("\n") + "\n";
}
