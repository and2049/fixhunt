// Run one hand-written program through the oracles (ground-truth checks and demos).
import { mkdirSync, readFileSync } from "node:fs";
import { basename, join } from "node:path";
import { RUNS_DIR } from "./config";
import { evaluateProgram } from "./oracles";
import { processFindings } from "./pipeline";
import type { Tool } from "./tools/types";

export async function checkFile(tool: Tool, rule: string, file: string, unsafe: boolean, report = false) {
  const info = await tool.ruleInfo(rule);
  const dir = join(RUNS_DIR, "check", `${tool.id}-${info.rule.replace(/[^\w.-]+/g, "_")}`);
  mkdirSync(dir, { recursive: true });
  const code = readFileSync(file, "utf8");
  const r = await evaluateProgram(tool, info, dir, { id: basename(file).replace(/\W+/g, "_"), title: basename(file), hazard: "manual", code, expectTrigger: true }, { unsafe });
  console.log(JSON.stringify({ rule: info.rule, fixKind: info.fixKind, fired: r.before.diagnostics.length, changed: r.after?.changed ?? false, findings: r.findings, error: r.error }, null, 2));
  if (r.after?.diff) console.log(r.after.diff);
  if (report && r.findings.some((f) => f.kind !== "disputed")) {
    const version = await tool.version();
    await processFindings(tool, info, version, dir, [r], unsafe);
  }
  return r;
}
