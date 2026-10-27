// Declarative tool adapters. A tool is a JSON spec (see tools/*.json and the README); this engine turns it
// into the `Tool` interface the pipeline uses. Nothing in the pipeline knows which linter it is driving.
import { existsSync, readFileSync } from "node:fs";
import { detectBwrap, exec, useContree, type ExecResult } from "../sandbox";
import type { Diagnostic, RuleInfo, Tool } from "./types";

export type Cmd = string[];
export type JsonParse = {
  format: "json"; items?: string; rule: string; message?: string; severity?: string; line?: string; col?: string; span?: string;
  fix?: string; fixMap?: Record<string, string>; fixPresent?: string; fixPresentKind?: string; rulePrefix?: string; nonJsonOk?: string;
};
export type RegexParse = { format: "regex"; pattern: string; fix?: string };
export type Parse = JsonParse | RegexParse;
export type Crash = { okExit?: number[]; stderrRegex?: string };
export type VarSpec = { env?: string; default?: string; candidates?: string[]; split?: boolean };

export type ToolSpec = {
  id: string; name?: string; language: string; ext: string; repo?: string; sandboxImage?: string; runnerHint?: string; docsFence?: string;
  vars?: Record<string, VarSpec>;
  env?: Record<string, string>;
  version: { cmd: Cmd; regex?: string; stripPrefix?: string; timeoutMs?: number };
  rule: {
    split?: string; upper?: boolean; cmd?: Cmd; timeoutMs?: number; idFromOutput?: string; failOnExit?: boolean;
    fixKind?: { regex?: string; map?: Record<string, string>; default?: string; onError?: string };
    docs?: { file?: string; url?: string; fallback?: string; prefix?: string };
  };
  lint: { cmd: Cmd; parse: Parse; crash?: Crash; timeoutMs?: number };
  fix: { cmd: Cmd; unsafeArgs?: string[]; crash?: Crash; fail?: { stderrRegex: string }; timeoutMs?: number; perFile?: boolean };
  check: { cmd: Cmd; sandboxCmd?: Cmd; timeoutMs?: number; isolate?: boolean };
  run: { pre?: Cmd; cmd: Cmd; sandboxCmd?: Cmd; env?: Record<string, string>; timeoutMs?: number; image?: string };
  repro?: string[];
  catalog?: { cmd: Cmd; parse: CatalogParse; timeoutMs?: number };
  sweep?: { fixKinds?: string[]; unsafeFixKinds?: string[]; languages?: string[]; skipRuleRegex?: string; requireNoteRegex?: string };
  config?: ConfigSpec;
};
/** How to read which rules a repository enables: a prefix list (toml), grouped rules (json) or a glob list (yaml). */
export type ConfigSpec = { files: string[]; format: "toml" | "json" | "yaml" | "opaque"; root?: Record<string, string>; select?: string[]; extend?: string[]; ignore?: string[]; families?: string[]; rules?: string; key?: string; default?: string[] | "recommended"; note?: string };
/** Configuration text that keeps a rule but turns its fix off. {rules} in the template is the items joined by sep; {rule}, {group}, {name} in an item. */
export type CatalogParse = { items?: string; rule: string; name?: string; fixKind?: string; recommended?: string; fixKindFrom?: { field: string; map: Array<{ regex: string; kind: string }>; default?: string }; note?: string; languages?: string[] | string; skipIf?: Array<{ field: string; regex: string }> };

const FIX_KINDS = ["safe", "unsafe", "none", "unknown"] as const;
const asFixKind = (s: unknown, d: RuleInfo["fixKind"] = "unknown"): RuleInfo["fixKind"] => (FIX_KINDS as readonly string[]).includes(String(s)) ? (s as RuleInfo["fixKind"]) : d;

/** Dot-path lookup with array indices and `$` for the root. */
export function path(obj: any, p?: string): any {
  if (p === undefined || p === "" || p === "$") return obj;
  let cur = obj;
  for (const k of p.replace(/^\$\.?/, "").split(".")) {
    if (cur == null) return undefined;
    cur = cur[k];
  }
  return cur;
}

function text(v: unknown): string {
  if (v == null) return "";
  if (Array.isArray(v)) return v.map((x) => (typeof x === "string" ? x : text((x as any)?.content ?? x))).join("");
  if (typeof v === "object") return String((v as any).content ?? (v as any).text ?? JSON.stringify(v));
  return String(v);
}

function expandHome(s: string) { return s.replace(/^~(?=\/|$)/, process.env.HOME ?? "~"); }

export class SpecTool implements Tool {
  id: string; language: string; ext: string; repo?: string; runnerHint?: string; docsFence?: string;
  private vars: Record<string, string[]> = {};
  constructor(public spec: ToolSpec, public source = "") {
    this.id = spec.id; this.language = spec.language; this.ext = spec.ext; this.repo = spec.repo; this.docsFence = spec.docsFence;
    for (const [k, v] of Object.entries(spec.vars ?? {})) {
      let val = (v.env && process.env[v.env]) || "";
      if (!val && v.candidates) val = v.candidates.find((c) => Bun.which(c)) ?? "";
      if (!val) val = v.default ?? "";
      val = expandHome(val);
      this.vars[k] = v.split ? val.split(/\s+/).filter(Boolean) : [val];
    }
    this.runnerHint = spec.runnerHint ?? this.render(spec.run.cmd, { file: `file.${spec.ext}` }).join(" ");
  }

  /** Expand {name} tokens; a token that is exactly a split var expands to several argv entries. */
  render(cmd: Cmd, ctx: Record<string, string>): string[] {
    const out: string[] = [];
    for (const tok of cmd) {
      const m = /^\{([\w.]+)\}$/.exec(tok);
      if (m && this.vars[m[1]] && this.vars[m[1]].length !== 1) { out.push(...this.vars[m[1]]); continue; }
      out.push(this.renderStr(tok, ctx));
    }
    return out;
  }
  renderStr(s: string, ctx: Record<string, string>): string {
    // Unknown placeholders are left as written, so literal braces in shell templates survive
    return s.replace(/\{([\w.]+)\}/g, (whole, k: string) => {
      if (k in ctx) return ctx[k];
      if (this.vars[k]) return this.vars[k].join(" ");
      if (k.startsWith("env.")) return process.env[k.slice(4)] ?? "";
      return whole;
    });
  }
  private ruleCtx(rule: string): Record<string, string> {
    const ctx: Record<string, string> = { rule };
    if (this.spec.rule.split) {
      const m = new RegExp(this.spec.rule.split).exec(rule);
      for (const [k, v] of Object.entries(m?.groups ?? {})) ctx[`rule.${k}`] = v ?? "";
    }
    return ctx;
  }
  private crashed(r: ExecResult, c?: Crash): boolean {
    const ok = c?.okExit ?? [0, 1];
    return r.timedOut || (r.code !== null && !ok.includes(r.code)) || (!!c?.stderrRegex && new RegExp(c.stderrRegex, "i").test(r.stderr));
  }
  private env(extra?: Record<string, string>): Record<string, string> | undefined {
    const e = { ...(this.spec.env ?? {}), ...(extra ?? {}) };
    return Object.keys(e).length ? e : undefined;
  }

  async version(): Promise<string> {
    const v = this.spec.version;
    const r = await exec(this.render(v.cmd, {}), { cwd: process.cwd(), timeoutMs: v.timeoutMs ?? 120_000, env: this.env() });
    let s = r.stdout.trim().split("\n").filter(Boolean).pop() ?? "unknown";
    if (v.regex) s = new RegExp(v.regex, "i").exec(r.stdout)?.[1] ?? s;
    if (v.stripPrefix) s = s.replace(new RegExp(v.stripPrefix, "i"), "");
    return s;
  }

  async ruleInfo(input: string): Promise<RuleInfo> {
    const sp = this.spec.rule;
    let rule = sp.upper ? input.toUpperCase() : input;
    let ctx = this.ruleCtx(rule);
    let out = "", code = 0;
    if (sp.cmd) {
      const r = await exec(this.render(sp.cmd, ctx), { cwd: process.cwd(), timeoutMs: sp.timeoutMs ?? 120_000, env: this.env() });
      out = r.stdout; code = r.code ?? 1;
      if (sp.idFromOutput) {
        const id = new RegExp(sp.idFromOutput, "m").exec(out)?.[1];
        if (!id) throw new Error(`${this.id}: unknown rule ${input}: ${(r.stderr || r.stdout).slice(0, 300)}`);
        rule = id; ctx = this.ruleCtx(rule);
      } else if (sp.failOnExit !== false && r.code !== 0) throw new Error(`${this.id}: rule lookup for ${input} failed: ${(r.stderr || r.stdout).slice(0, 300)}`);
    }
    let docs = "";
    if (sp.docs?.file) { const f = this.renderStr(sp.docs.file, ctx); if (f && existsSync(f)) docs = readFileSync(f, "utf8"); }
    if (!docs && sp.docs?.url) {
      try { const res = await fetch(this.renderStr(sp.docs.url, ctx), { signal: AbortSignal.timeout(20_000) }); if (res.ok) docs = await res.text(); } catch {}
    }
    if (docs && out.trim()) docs = `${out.trim()}\n\n${docs}`; // command output (labels, summary) ahead of fetched docs
    if (!docs) docs = out;
    if (!docs) docs = this.renderStr(sp.docs?.fallback ?? `Rule {rule} of ${this.id}. No documentation found; infer from the name.`, ctx);
    if (sp.docs?.prefix) docs = this.renderStr(sp.docs.prefix, ctx) + docs;
    let fixKind: RuleInfo["fixKind"] = asFixKind(sp.fixKind?.default, "unknown");
    if (sp.fixKind?.regex) {
      const m = new RegExp(sp.fixKind.regex, "m").exec(out)?.[1]?.toLowerCase();
      if (m) fixKind = asFixKind(sp.fixKind.map?.[m] ?? m, fixKind);
      else if (code !== 0 && sp.fixKind.onError) fixKind = asFixKind(sp.fixKind.onError, fixKind);
    }
    return { tool: this.id, rule, fixKind, docs };
  }

  private parseDiagnostics(p: Parse, r: ExecResult, rule: string): { diagnostics: Diagnostic[]; invalid: boolean } {
    const diagnostics: Diagnostic[] = [];
    if (p.format === "regex") {
      for (const m of r.stdout.matchAll(new RegExp(p.pattern, "gm"))) {
        const g = m.groups ?? {};
        const id = g.rule ?? rule;
        if (id !== rule) continue;
        const line = g.line ? Number(g.line) : undefined, col = g.col ? Number(g.col) : undefined;
        diagnostics.push({ rule: id, severity: g.severity ?? "warning", message: g.message ?? "", span: line !== undefined ? [line, col ?? 0] : null, fix: asFixKind(p.fix, "unknown") });
      }
      return { diagnostics, invalid: false };
    }
    let j: any;
    try { j = JSON.parse(r.stdout); } catch {
      return { diagnostics, invalid: !(p.nonJsonOk && new RegExp(p.nonJsonOk).test(r.stdout + r.stderr)) };
    }
    const items = path(j, p.items);
    // The output parsed but does not have the expected shape: a tool failure, not a clean run
    if (!Array.isArray(items)) return { diagnostics, invalid: !(p.nonJsonOk && new RegExp(p.nonJsonOk).test(r.stdout + r.stderr)) };
    for (const d of items) {
      let id = text(path(d, p.rule));
      if (!id) continue;
      if (p.rulePrefix) { if (!id.startsWith(p.rulePrefix)) continue; id = id.slice(p.rulePrefix.length); }
      if (id !== rule) continue; // only the rule under test, same as the regex parser
      const line = p.line ? Number(path(d, p.line)) : NaN, col = p.col ? Number(path(d, p.col)) : 0;
      const spanV = p.span ? path(d, p.span) : undefined;
      const span: Diagnostic["span"] = Array.isArray(spanV) ? [Number(spanV[0]), Number(spanV[1])] : Number.isFinite(line) ? [line, col] : null;
      let fix: Diagnostic["fix"] = undefined;
      if (p.fix) {
        const v = path(d, p.fix);
        const mapped = v == null ? undefined : (p.fixMap ?? {})[String(v)] ?? String(v);
        fix = mapped !== undefined && (FIX_KINDS as readonly string[]).includes(mapped) ? (mapped as Diagnostic["fix"]) : p.fixPresent && path(d, p.fixPresent) != null ? asFixKind(p.fixPresentKind, "unknown") : "none";
      }
      diagnostics.push({ rule: id, severity: text(path(d, p.severity)) || "warning", message: text(path(d, p.message)), span, fix });
    }
    return { diagnostics, invalid: false };
  }

  async lint(file: string, rule: string, cwd: string) {
    const l = this.spec.lint;
    const r = await exec(this.render(l.cmd, { ...this.ruleCtx(rule), file, dir: cwd }), { cwd, timeoutMs: l.timeoutMs ?? 120_000, env: this.env() });
    const { diagnostics, invalid } = this.parseDiagnostics(l.parse, r, rule);
    return { diagnostics, crashed: invalid || this.crashed(r, l.crash), raw: r };
  }

  async fix(file: string, rule: string, cwd: string, unsafe: boolean) {
    const f = this.spec.fix;
    const cmd = this.render(f.cmd, { ...this.ruleCtx(rule), file, dir: cwd });
    if (unsafe && f.unsafeArgs) cmd.splice(cmd.length - 1, 0, ...f.unsafeArgs); // before the file argument
    const r = await exec(cmd, { cwd, timeoutMs: f.timeoutMs ?? 120_000, env: this.env() });
    // `fail`: the fixer ran but could not apply fixes (clang-tidy on a file that does not compile); not a crash
    const failed = f.fail && new RegExp(f.fail.stderrRegex).test(r.stderr) ? ((r.stdout + "\n" + r.stderr).split("\n").find((l) => /: error: /.test(l)) ?? r.stderr.split("\n")[0] ?? "").replace(/^.*?\/(?=[^/]+:\d+:\d+: )/, "").slice(0, 200) : undefined;
    return { crashed: this.crashed(r, f.crash), failed, raw: r };
  }

  async check(file: string, cwd: string) {
    const c = this.spec.check;
    // `isolate` runs the checker under bwrap (compilers see untrusted source). Where bwrap is missing (the hosted
    // container) and the spec gives a sandbox command, the check runs in the tool's sandbox image instead.
    const image = this.spec.sandboxImage;
    if (c.isolate && c.sandboxCmd && image && !(await detectBwrap()) && (await useContree())) return exec(this.render(c.sandboxCmd, { file, dir: cwd }), { cwd, timeoutMs: Math.max(c.timeoutMs ?? 60_000, 60_000), isolate: true, image, env: this.env() });
    return exec(this.render(c.cmd, { file, dir: cwd }), { cwd, timeoutMs: c.timeoutMs ?? 60_000, env: this.env(), isolate: !!c.isolate });
  }

  async run(file: string, cwd: string) {
    const ru = this.spec.run;
    const ctx = { file, dir: cwd, exe: file.replace(/\.[^.]+$/, "") + ".bin" };
    const env = this.env(ru.env);
    const image = ru.image ?? this.spec.sandboxImage;
    if (ru.sandboxCmd && image && (await useContree())) {
      return exec(this.render(ru.sandboxCmd, ctx), { cwd, timeoutMs: Math.max(ru.timeoutMs ?? 5_000, 60_000), isolate: true, image, env });
    }
    if (ru.pre) {
      const c = await exec(this.render(ru.pre, ctx), { cwd, timeoutMs: 120_000, env: this.env(), isolate: true });
      if (c.code !== 0) return { ...c, stderr: "compile failed: " + c.stderr };
    }
    return exec(this.render(ru.cmd, ctx), { cwd, timeoutMs: ru.timeoutMs ?? 5_000, isolate: true, image, env });
  }

  reproCommands(rule: string, file: string, unsafe: boolean): string[] {
    const ctx = { ...this.ruleCtx(rule), file, unsafe: unsafe ? " " + (this.spec.fix.unsafeArgs ?? []).join(" ") : "", exe: file.replace(/\.[^.]+$/, "") + ".bin" };
    const lines = this.spec.repro ?? [this.render(this.spec.run.cmd, ctx).join(" "), this.render(this.spec.fix.cmd, ctx).join(" ") + ctx.unsafe, this.render(this.spec.run.cmd, ctx).join(" ")];
    return lines.map((l) => this.renderStr(l, ctx));
  }

  /** Rule catalog from the spec's catalog command. */
  async catalog(): Promise<Array<{ rule: string; fixKind: RuleInfo["fixKind"]; languages?: string[]; name?: string; note?: string; recommended?: boolean }>> {
    const c = this.spec.catalog;
    if (!c) throw new Error(`${this.id}: the tool spec has no catalog command`);
    const r = await exec(this.render(c.cmd, {}), { cwd: process.cwd(), timeoutMs: c.timeoutMs ?? 600_000, maxOutput: 64 * 1024 * 1024, env: this.env() });
    if (r.code !== 0) throw new Error(`${this.id}: catalog command failed: ${r.stderr.slice(0, 300)}`);
    const items = path(JSON.parse(r.stdout), c.parse.items);
    const out: Array<{ rule: string; fixKind: RuleInfo["fixKind"]; languages?: string[]; name?: string; note?: string; recommended?: boolean }> = [];
    for (const d of Array.isArray(items) ? items : []) {
      if ((c.parse.skipIf ?? []).some((s) => new RegExp(s.regex, "i").test(text(path(d, s.field))))) continue;
      const rule = text(path(d, c.parse.rule));
      if (!rule) continue;
      let fixKind: RuleInfo["fixKind"] = "unknown";
      if (c.parse.fixKind) fixKind = asFixKind(path(d, c.parse.fixKind));
      else if (c.parse.fixKindFrom) {
        const v = text(path(d, c.parse.fixKindFrom.field));
        fixKind = asFixKind(c.parse.fixKindFrom.map.find((m) => new RegExp(m.regex, "i").test(v))?.kind ?? c.parse.fixKindFrom.default);
      }
      const langs = Array.isArray(c.parse.languages) ? c.parse.languages : c.parse.languages ? path(d, c.parse.languages) : undefined;
      out.push({ rule, fixKind, name: c.parse.name ? text(path(d, c.parse.name)) : undefined, note: c.parse.note ? text(path(d, c.parse.note)) : undefined, languages: Array.isArray(langs) ? langs.map(String) : undefined, recommended: c.parse.recommended ? path(d, c.parse.recommended) === true : undefined });
    }
    return out;
  }
}

export function loadSpec(file: string): SpecTool {
  const spec = JSON.parse(readFileSync(file, "utf8")) as ToolSpec;
  for (const k of ["id", "language", "ext", "version", "rule", "lint", "fix", "check", "run"] as const) if (!(k in spec)) throw new Error(`${file}: tool spec is missing "${k}"`);
  return new SpecTool(spec, file);
}
