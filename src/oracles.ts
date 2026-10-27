// Model-free oracles. Each program goes through: run → lint → fix (safe) → check → run → re-lint.
import { mkdirSync, writeFileSync, copyFileSync, rmSync } from "node:fs";
import { createHash } from "node:crypto";
import { join, resolve } from "node:path";
import { exec, type ExecResult } from "./sandbox";
import type { Diagnostic, RuleInfo, Tool } from "./tools/types";

export type FindingKind =
  | "tool-crash"          // O1
  | "fix-breaks-syntax"   // O2
  | "fix-changes-behavior" // O3
  | "fix-not-fixpoint"    // O4 rule still fires after its own fix
  | "fix-introduces-diagnostic" // O4 new diagnostics of the same rule appear after fix
  | "disputed";           // prediction ≠ observation, no oracle hit → model judge

export type Finding = { kind: FindingKind; safeLabel: boolean; detail: string };

export type Prediction = { expectTrigger: boolean };

export type ProgramResult = {
  id: string;
  title: string;
  hazard: string;
  rule: string;
  predicted: Prediction;
  before: { diagnostics: Diagnostic[]; run: Snap; checkOk: boolean };
  after?: { changed: boolean; diagnostics: Diagnostic[]; run: Snap; checkOk: boolean; diff: string };
  findings: Finding[];
  error?: string;
};

export type Snap = { stdout: string; stderr1: string; code: number | null; timedOut: boolean; stdoutHash?: string };

const DISPLAY = 16 * 1024; // stored/displayed stdout; comparisons use the hash of the full normalized output

function snap(r: ExecResult, wd: string): Snap {
  const full = normalize(r.stdout, wd);
  return { stdout: full.length > DISPLAY ? full.slice(0, DISPLAY) + `\n...[${full.length - DISPLAY} more bytes]` : full, stdoutHash: createHash("sha256").update(full).digest("hex").slice(0, 24), stderr1: normalize(firstErrorLine(r.stderr), wd), code: r.code, timedOut: r.timedOut };
}

const infraFailure = (r: ExecResult) => /^(bwrap:|sandbox failure:)/m.test(r.stderr);

/** Scrub run-location noise: absolute paths of the working dir and line:column positions attached to them. */
function normalize(s: string, wd: string): string {
  const abs = resolve(wd);
  return s
    .split("file://" + abs).join("<wd>")
    .split(abs).join("<wd>")
    .replace(/<wd>[^\s:)]*(?::\d+){1,2}/g, "<wd>/prog")
    .replace(/<wd>[^\s:)]*/g, "<wd>/prog");
}

function firstErrorLine(stderr: string): string {
  // Node prints a stack; keep the "TypeError: ..." style line only, so line numbers in stacks don't cause noise
  const m = /^(\w*Error[^\n]*)$/m.exec(stderr);
  return m ? m[1] : stderr.split("\n").find((l) => l.trim()) ?? "";
}

function sameBehavior(a: Snap, b: Snap): boolean {
  const out = a.stdoutHash && b.stdoutHash ? a.stdoutHash === b.stdoutHash : a.stdout === b.stdout;
  return out && a.code === b.code && a.timedOut === b.timedOut && a.stderr1 === b.stderr1;
}

export async function evaluateProgram(
  tool: Tool,
  info: RuleInfo,
  dir: string,
  p: { id: string; title: string; hazard: string; code: string; expectTrigger: boolean },
  opts: { unsafe: boolean },
): Promise<ProgramResult> {
  const wd = join(dir, p.id);
  mkdirSync(wd, { recursive: true });
  const orig = `orig.${tool.ext}`;
  const fixed = `fixed.${tool.ext}`;
  const prog = `prog.${tool.ext}`; // both versions execute under this one name
  writeFileSync(join(wd, orig), p.code);
  // Every execution gets a fresh directory holding only the program, so one run cannot leave state for the next
  let runNo = 0;
  const runAs = async (src: string) => {
    const rd = join(wd, `run${++runNo}`);
    rmSync(rd, { recursive: true, force: true });
    mkdirSync(rd, { recursive: true });
    copyFileSync(join(wd, src), join(rd, prog));
    const r = await tool.run(prog, rd);
    rmSync(rd, { recursive: true, force: true });
    return r;
  };
  const res: ProgramResult = {
    id: p.id, title: p.title, hazard: p.hazard, rule: info.rule,
    predicted: { expectTrigger: p.expectTrigger },
    before: { diagnostics: [], run: { stdout: "", stderr1: "", code: null, timedOut: false }, checkOk: false },
    findings: [],
  };
  let safeLabel = !opts.unsafe && info.fixKind === "safe";

  // Before: must be valid and deterministic (run twice)
  const chk = await tool.check(orig, wd);
  if (chk.timedOut || infraFailure(chk)) { res.error = "syntax check did not complete: " + (chk.timedOut ? "timed out" : chk.stderr.split("\n")[0]); return res; }
  res.before.checkOk = chk.code === 0;
  if (!res.before.checkOk) { res.error = "generated program does not parse: " + chk.stderr.slice(0, 300); return res; }
  const raw1 = await runAs(orig);
  if (infraFailure(raw1)) { res.error = "sandbox failure: " + raw1.stderr.split("\n")[0].replace(/^sandbox failure: /, ""); return res; }
  const r1 = snap(raw1, wd);
  if (r1.timedOut) { res.error = "generated program does not terminate within the time limit"; return res; }
  const raw2 = await runAs(orig);
  if (infraFailure(raw2)) { res.error = "sandbox failure: " + raw2.stderr.split("\n")[0].replace(/^sandbox failure: /, ""); return res; }
  const r2 = snap(raw2, wd);
  if (!sameBehavior(r1, r2)) { res.error = "generated program is not deterministic"; return res; }
  res.before.run = r1;

  const l1 = await tool.lint(orig, info.rule, wd);
  res.before.diagnostics = l1.diagnostics;
  if (l1.crashed) {
    res.findings.push({ kind: "tool-crash", safeLabel, detail: "lint crashed: " + (l1.raw.stderr || l1.raw.stdout).slice(0, 500) });
    return res;
  }
  const fired = l1.diagnostics.length > 0;
  // Tools that label fixes per diagnostic (ruff) override the rule-level label
  if (!opts.unsafe && l1.diagnostics.some((d) => d.fix === "safe")) safeLabel = true;
  if (!opts.unsafe && l1.diagnostics.length && l1.diagnostics.every((d) => d.fix === "unsafe" || d.fix === "none")) safeLabel = false;
  if (fired !== p.expectTrigger) {
    res.findings.push({ kind: "disputed", safeLabel, detail: `model expected the rule to ${p.expectTrigger ? "fire" : "stay silent"}, it ${fired ? "fired" : "stayed silent"}` });
  }
  if (!fired) return res;

  // Apply the fix
  copyFileSync(join(wd, orig), join(wd, fixed));
  const f = await tool.fix(fixed, info.rule, wd, opts.unsafe);
  if (f.crashed) {
    res.findings.push({ kind: "tool-crash", safeLabel, detail: "fix crashed: " + (f.raw.stderr || f.raw.stdout).slice(0, 500) });
    return res;
  }
  if (f.failed) { res.error = "fixer could not apply the fix: " + f.failed; return res; }
  const diffR = await exec(["diff", "-u", orig, fixed], { cwd: wd, timeoutMs: 10_000 });
  const changed = diffR.code === 1;
  const after: NonNullable<ProgramResult["after"]> = { changed, diagnostics: [], run: r1, checkOk: true, diff: diffR.stdout };
  res.after = after;
  if (!changed) return res; // rule fired but offers no fix here; nothing to test

  const chk2 = await tool.check(fixed, wd);
  if (chk2.timedOut || infraFailure(chk2)) { res.error = "syntax check of the fixed program did not complete: " + (chk2.timedOut ? "timed out" : chk2.stderr.split("\n")[0]); return res; }
  after.checkOk = chk2.code === 0;
  if (!after.checkOk) {
    res.findings.push({ kind: "fix-breaks-syntax", safeLabel, detail: chk2.stderr.slice(0, 500) });
    return res;
  }
  // The fixed program also runs twice: an infrastructure failure or nondeterminism must not become a finding
  const rawA = await runAs(fixed);
  if (infraFailure(rawA)) { res.error = "sandbox failure while running the fixed program: " + rawA.stderr.split("\n")[0].replace(/^sandbox failure: /, ""); return res; }
  after.run = snap(rawA, wd);
  if (!sameBehavior(r1, after.run)) {
    const rawB = await runAs(fixed);
    if (infraFailure(rawB)) { res.error = "sandbox failure while running the fixed program: " + rawB.stderr.split("\n")[0].replace(/^sandbox failure: /, ""); return res; }
    if (!sameBehavior(after.run, snap(rawB, wd))) { res.error = "fixed program is not deterministic"; return res; }
    res.findings.push({ kind: "fix-changes-behavior", safeLabel, detail: describeDiff(r1, after.run) });
  }
  const l2 = await tool.lint(fixed, info.rule, wd);
  after.diagnostics = l2.diagnostics;
  if (l2.crashed) {
    res.findings.push({ kind: "tool-crash", safeLabel, detail: "re-lint crashed: " + (l2.raw.stderr || l2.raw.stdout).slice(0, 500) });
    return res;
  }
  if (l2.diagnostics.length > l1.diagnostics.length) {
    res.findings.push({ kind: "fix-introduces-diagnostic", safeLabel, detail: `${l1.diagnostics.length} diagnostic(s) before, ${l2.diagnostics.length} after the fix` });
  }
  // Idempotence: applying the fix again must not change the file further
  const fixed2 = `fixed2.${tool.ext}`;
  copyFileSync(join(wd, fixed), join(wd, fixed2));
  const f2 = await tool.fix(fixed2, info.rule, wd, opts.unsafe);
  if (!f2.crashed) {
    const d2 = await exec(["diff", "-u", fixed, fixed2], { cwd: wd, timeoutMs: 10_000 });
    if (d2.code === 1) res.findings.push({ kind: "fix-not-fixpoint", safeLabel, detail: `applying the fix a second time changes the file again:\n${d2.stdout.slice(0, 800)}` });
    else if (l2.diagnostics.length && l2.diagnostics.length <= l1.diagnostics.length && !res.findings.some((f) => f.kind === "fix-introduces-diagnostic")) res.findings.push({ kind: "fix-not-fixpoint", safeLabel, detail: `the rule still reports ${l2.diagnostics.length} diagnostic(s) after its fix, and a second fix does not remove them` });
  }
  return res;
}

function describeDiff(a: Snap, b: Snap): string {
  const parts: string[] = [];
  if (a.stdout !== b.stdout) parts.push(`stdout before:\n${a.stdout.trimEnd()}\nstdout after:\n${b.stdout.trimEnd()}`);
  if (a.code !== b.code || a.timedOut !== b.timedOut) parts.push(`exit ${a.timedOut ? "timeout" : a.code} → ${b.timedOut ? "timeout" : b.code}`);
  if (a.stderr1 !== b.stderr1) parts.push(`stderr before: ${a.stderr1 || "(none)"}\nstderr after: ${b.stderr1 || "(none)"}`);
  return parts.join("\n");
}
