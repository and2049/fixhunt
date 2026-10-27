// Rule catalogs: which rules exist, whether they have a fix and how the tool labels it. Built from the tool
// spec's catalog command and cached in data/<tool>-rules.json.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import type { SpecTool } from "./tools/spec";

export type CatalogRule = { rule: string; fixKind: "safe" | "unsafe" | "none" | "unknown"; languages?: string[]; name?: string; note?: string; recommended?: boolean };

export const catalogPath = (toolId: string) => `data/${toolId}-rules.json`;

export async function catalogFor(tool: SpecTool, refresh = false): Promise<CatalogRule[]> {
  const out = catalogPath(tool.id);
  const version = await tool.version();
  if (!refresh && existsSync(out)) {
    const j = JSON.parse(readFileSync(out, "utf8"));
    if (Array.isArray(j)) return j; // older cache without a version stamp
    if (j.version === version) return j.rules;
    console.log(`catalog for ${tool.id} was built with ${j.version}; rebuilding for ${version}`);
  }
  const rules = await tool.catalog();
  mkdirSync("data", { recursive: true });
  writeFileSync(out, JSON.stringify({ version, rules }, null, 1));
  return rules;
}

/** Rules a sweep should hunt, per the spec's sweep section. */
export function sweepRules(tool: SpecTool, catalog: CatalogRule[], unsafe: boolean): CatalogRule[] {
  const sw = tool.spec.sweep ?? {};
  const kinds = unsafe ? sw.unsafeFixKinds ?? ["safe", "unsafe", "unknown"] : sw.fixKinds ?? ["safe"];
  let rules = catalog.filter((r) => kinds.includes(r.fixKind));
  if (sw.languages?.length) rules = rules.filter((r) => !r.languages?.length || r.languages.some((l) => sw.languages!.includes(l)));
  if (sw.requireNoteRegex && !unsafe) rules = rules.filter((r) => new RegExp(sw.requireNoteRegex!, "i").test(r.note ?? ""));
  if (sw.skipRuleRegex) rules = rules.filter((r) => !new RegExp(sw.skipRuleRegex!).test(r.rule));
  return rules;
}
