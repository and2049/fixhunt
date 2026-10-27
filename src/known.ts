// Known-risk check: which of the rules a repository enables already have a verified finding (a fix that changed
// behaviour on a generated program) in the findings bank. Model-free; runs before any sandbox work.
import { existsSync, lstatSync, readFileSync } from "node:fs";
import { join } from "node:path";
import type { CatalogRule } from "./catalog";
import type { ConfigSpec, SpecTool } from "./tools/spec";
import { findings as loadFindings, type Finding } from "./web/data";

export type Enabled = { file?: string; rules?: Set<string>; note?: string };

const GRADE_ORDER: Record<string, number> = { real: 0, unclear: 1, unjudged: 2, "intended-change": 3, "introspection-only": 4, "program-bug": 5 };
const SEV_ORDER: Record<string, number> = { high: 0, medium: 1, low: 2, "-": 3 };

// ---------------------------------------------------------------------------------------------- enabled rules

function getPath(o: any, p: string): any { return p.split(".").reduce((a, k) => (a == null ? undefined : a[k]), o); }

/** JSON with comments and trailing commas (biome.jsonc, tsconfig style). */
function stripJsonc(s: string): string {
  let out = "", i = 0, inStr = false;
  while (i < s.length) {
    const c = s[i];
    if (inStr) { out += c; if (c === "\\") { out += s[i + 1] ?? ""; i += 2; continue; } if (c === '"') inStr = false; i++; continue; }
    if (c === '"') { inStr = true; out += c; i++; continue; }
    if (c === "/" && s[i + 1] === "/") { while (i < s.length && s[i] !== "\n") i++; continue; }
    if (c === "/" && s[i + 1] === "*") { i += 2; while (i < s.length && !(s[i] === "*" && s[i + 1] === "/")) i++; i += 2; continue; }
    out += c; i++;
  }
  return out.replace(/,(\s*[}\]])/g, "$1");
}

const list = (v: unknown): string[] => (Array.isArray(v) ? v.map(String) : typeof v === "string" ? [v] : []);

/** Prefix-selected rule codes (ruff): select/extend-select/ignore lists of code prefixes, "ALL" for everything. */
function byPrefix(doc: any, c: ConfigSpec, ids: string[]): Set<string> {
  const first = (paths: string[] | undefined) => { for (const p of paths ?? []) { const v = getPath(doc, p); if (v !== undefined) return list(v); } return undefined; };
  const union = (paths: string[] | undefined) => (paths ?? []).flatMap((p) => list(getPath(doc, p)));
  const select = [...(first(c.select) ?? (Array.isArray(c.default) ? c.default : [])), ...union(c.extend)];
  const ignore = union(c.ignore);
  // A prefix made of letters selects a linter, and must end where the code's letters end ("F" is not "FURB"),
  // except the families the spec names ("PL" covers PLC, PLE, PLR, PLW); a prefix ending in a digit is a code prefix.
  const families = c.families ?? [];
  const match = (p: string, id: string) => p === "ALL" || (id.startsWith(p) && (/\d$/.test(p) || p.length === id.length || /\d/.test(id[p.length]) || families.includes(p)));
  const hit = (ps: string[], id: string) => ps.some((p) => match(p, id));
  // ruff resolves conflicts by prefix length; the longer, more specific prefix wins
  const longest = (ps: string[], id: string) => Math.max(0, ...ps.filter((p) => match(p, id)).map((p) => (p === "ALL" ? 0 : p.length)));
  return new Set(ids.filter((id) => hit(select, id) && (!hit(ignore, id) || longest(select, id) > longest(ignore, id))));
}

/** Grouped rules (Biome): linter.rules.<group>.<rule> = "off" | "on" | level | { level, fix }, plus the recommended set. */
function byGroups(rules: any, c: ConfigSpec, catalog: CatalogRule[]): Set<string> {
  const on = new Set<string>();
  const recommendedOff = rules?.recommended === false;
  if (rules?.all === true) catalog.forEach((r) => on.add(r.rule));
  else if (c.default === "recommended" && !recommendedOff) catalog.filter((r) => r.recommended).forEach((r) => on.add(r.rule));
  for (const [group, v] of Object.entries(rules ?? {})) {
    if (group === "recommended" || group === "all" || typeof v !== "object" || v === null) continue;
    const g = v as Record<string, unknown>;
    if (g.recommended === false) for (const r of catalog) if (r.rule.startsWith(`${group}/`) && r.recommended) on.delete(r.rule);
    if (g.recommended === true) for (const r of catalog) if (r.rule.startsWith(`${group}/`) && r.recommended) on.add(r.rule);
    if (g.all === true) for (const r of catalog) if (r.rule.startsWith(`${group}/`)) on.add(r.rule);
    for (const [name, val] of Object.entries(g)) {
      if (name === "recommended" || name === "all") continue;
      const id = `${group}/${name}`;
      const level = typeof val === "string" ? val : typeof val === "object" && val !== null ? String((val as any).level ?? "on") : "on";
      if (level === "off") on.delete(id); else on.add(id);
    }
  }
  return on;
}

/** Glob list with negation, in order (clang-tidy Checks): "-*,modernize-*,-modernize-use-trailing-return-type". */
function byGlob(patterns: string[], ids: string[]): Set<string> {
  const on = new Set<string>();
  for (const raw of patterns.flatMap((p) => p.split(","))) {
    const p = raw.trim();
    if (!p) continue;
    const neg = p.startsWith("-");
    const re = new RegExp(`^${p.slice(neg ? 1 : 0).replace(/[.+?^${}()|[\]\\]/g, "\\$&").replace(/\*/g, ".*")}$`);
    for (const id of ids) if (re.test(id)) { if (neg) on.delete(id); else on.add(id); }
  }
  return on;
}

/** The value of one top-level YAML key: a scalar (quoted or not), a folded/literal block, or a list. */
function yamlValue(text: string, key: string): string[] | undefined {
  const lines = text.split(/\r?\n/);
  const i = lines.findIndex((l) => new RegExp(`^${key}\\s*:`).test(l));
  if (i < 0) return undefined;
  const rest = lines[i].replace(new RegExp(`^${key}\\s*:\\s*`), "").replace(/\s+#.*$/, "").trim();
  const block = () => { const out: string[] = []; for (let j = i + 1; j < lines.length && /^\s+\S/.test(lines[j]); j++) out.push(lines[j].trim()); return out; };
  if (rest === ">" || rest === "|" || rest === ">-" || rest === "|-") return [block().join(rest.startsWith(">") ? " " : "\n")];
  if (rest === "") return block().map((l) => l.replace(/^-\s*/, "").replace(/^['"]|['"]$/g, ""));
  if (rest.startsWith("[")) { // flow list, possibly continued on the following lines up to the closing bracket
    let text2 = rest;
    if (!rest.includes("]")) for (let j = i + 1; j < lines.length; j++) { text2 += " " + lines[j].trim(); if (lines[j].includes("]")) break; }
    return text2.slice(1, text2.indexOf("]") < 0 ? undefined : text2.indexOf("]")).split(",").map((x) => x.trim().replace(/^['"]|['"]$/g, "")).filter(Boolean);
  }
  return [rest.replace(/^['"]|['"]$/g, "")];
}

/** Rules the repository's own configuration enables for this tool, per the spec's `config` section. */
export function enabledRules(tool: SpecTool, dir: string, catalog: CatalogRule[]): Enabled {
  const c = tool.spec.config;
  if (!c) return { note: "no configuration reader in the tool spec; every rule with a finding is listed" };
  const ids = catalog.map((r) => r.rule);
  for (const f of c.files) {
    const p = join(dir, f);
    if (!existsSync(p)) continue;
    if (c.format === "opaque") return { file: f, note: c.note ?? `${f} is not read; every rule with a finding is listed` };
    // Only a bounded regular file is read: the repository is untrusted (a link to a device, a huge file)
    try { const st = lstatSync(p); if (!st.isFile() || st.size > 1_000_000) return { file: f, note: `${f} is not a regular file under 1 MB; every rule with a finding is listed` }; } catch { continue; }
    let text: string;
    try { text = readFileSync(p, "utf8"); } catch { continue; }
    const unresolved = (what: string) => ({ file: f, note: `${f} uses ${what}, which is not resolved; every rule with a finding is listed` });
    try {
      if (c.format === "toml") {
        let doc: any = Bun.TOML.parse(text);
        const root = c.root?.[f];
        if (root) { doc = getPath(doc, root); if (doc === undefined) continue; } // pyproject.toml without a [tool.x] table: look further
        if (doc && typeof doc === "object" && "extend" in doc) return unresolved("extend");
        return { file: f, rules: byPrefix(doc, c, ids) };
      }
      if (c.format === "json") {
        const doc = JSON.parse(stripJsonc(text));
        if (doc?.extends !== undefined || (Array.isArray(doc?.overrides) && doc.overrides.length)) return unresolved(doc?.extends !== undefined ? "extends" : "overrides");
        if (doc?.linter?.enabled === false) return { file: f, rules: new Set(), note: `${f} disables the linter` };
        return { file: f, rules: byGroups(getPath(doc, c.rules ?? "") ?? {}, c, catalog) };
      }
      if (c.format === "yaml") return { file: f, rules: byGlob(yamlValue(text, c.key ?? "Checks") ?? (Array.isArray(c.default) ? c.default : []), ids) };
    } catch (e) { return { file: f, note: `${f} could not be read (${String((e as Error).message ?? e).split("\n")[0].slice(0, 80)}); every rule with a finding is listed` }; }
  }
  const note = "no configuration file; the tool's defaults";
  if (c.format === "toml") return { rules: byPrefix({}, c, ids), note };
  if (c.format === "json") return { rules: byGroups({}, c, catalog), note };
  if (c.format === "yaml") return { rules: byGlob(Array.isArray(c.default) ? c.default : [], ids), note };
  return { note: c.note };
}

// ---------------------------------------------------------------------------------------------- findings bank

export type BankEntry = {
  tool: string; rule: string; findings: number; safe: number; grade: string; severity: string;
  /** How many of the findings have a minimized program that reproduced in a fresh sandbox (recorded on newer runs only) */
  confirmed: number;
  urls: Array<{ url: string; relation: string }>; runId: string; programId: string;
};

const BEHAVIOUR_KINDS = new Set(["fix-changes-behavior", "fix-breaks-syntax"]);
// Every finding was observed in a sandbox when it was made; `confirmed` additionally records that the minimized
// program reproduced it in a fresh sandbox (older runs did not record this, so they count as not re-verified)
const isBehaviour = (f: Finding) => BEHAVIOUR_KINDS.has(f.report.kind) && (f.report.evidence as any)?.confirmed !== false;
const isConfirmed = (f: Finding) => (f.report.evidence as any)?.confirmed === true;

/** One entry per (tool, rule) with at least one behaviour or build change, keyed "tool|rule"; the best-graded finding is the link. */
export function bank(fs: Finding[] = loadFindings()): Map<string, BankEntry> {
  const out = new Map<string, BankEntry>();
  const better = (a: Finding, b: BankEntry) => (GRADE_ORDER[a.grade] ?? 9) - (GRADE_ORDER[b.grade] ?? 9) || (SEV_ORDER[a.severity] ?? 9) - (SEV_ORDER[b.severity] ?? 9);
  for (const f of fs) {
    if (!isBehaviour(f)) continue;
    const key = `${f.run.tool}|${f.run.rule.rule}`;
    const e = out.get(key);
    const urls = f.report.duplicates.filter((d) => d.relation !== "unrelated");
    if (!e) { out.set(key, { tool: f.run.tool, rule: f.run.rule.rule, findings: 1, confirmed: Number(isConfirmed(f)), safe: Number(f.report.safeLabel), grade: f.grade, severity: f.severity, urls: [...urls], runId: f.run.id, programId: f.report.programId }); continue; }
    e.findings++; e.confirmed += Number(isConfirmed(f)); e.safe += Number(f.report.safeLabel);
    for (const u of urls) if (!e.urls.some((x) => x.url === u.url)) e.urls.push(u);
    if (better(f, e) < 0) { e.grade = f.grade; e.severity = f.severity; e.runId = f.run.id; e.programId = f.report.programId; }
  }
  return out;
}

export type RiskRule = BankEntry & { fixKind: string };
export type Risk = { file?: string; enabled?: number; note?: string; known: RiskRule[]; notEnabled: number };

/** Rules the repository enables that have a finding in the bank, most severe first. */
export function riskCheck(tool: SpecTool, dir: string, catalog: CatalogRule[], b: Map<string, BankEntry> = bank()): Risk {
  // Without a catalog the configuration cannot be resolved to rule ids: list every rule with a finding rather than claim none is enabled
  const en: Enabled = catalog.length ? enabledRules(tool, dir, catalog) : { file: tool.spec.config?.files.find((f) => existsSync(join(dir, f))), note: "rule catalog unavailable; every rule with a finding is listed" };
  const kinds = new Map(catalog.map((r) => [r.rule, r.fixKind]));
  const all = [...b.values()].filter((e) => e.tool === tool.id).map((e) => ({ ...e, fixKind: kinds.get(e.rule) ?? "unknown" }));
  const known = (en.rules ? all.filter((e) => en.rules!.has(e.rule)) : all).sort((a, b2) => (GRADE_ORDER[a.grade] ?? 9) - (GRADE_ORDER[b2.grade] ?? 9) || (SEV_ORDER[a.severity] ?? 9) - (SEV_ORDER[b2.severity] ?? 9) || b2.findings - a.findings || a.rule.localeCompare(b2.rule));
  return { file: en.file, enabled: en.rules?.size, note: en.note, known, notEnabled: all.length - known.length };
}

