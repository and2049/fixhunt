// Stage 5: MINIMIZE. Line-level delta debugging with the oracle as the test. No model needed.
import { evaluateProgram, type FindingKind, type ProgramResult } from "./oracles";
import type { RuleInfo, Tool } from "./tools/types";
import { withLocalSandbox } from "./sandbox";
import { chat } from "./llm";
import { MODELS } from "./config";

export type MinimizeResult = { code: string; lines: { before: number; after: number }; evaluations: number; result: ProgramResult; proposal?: "accepted" | "rejected" | "skipped"; cost: number };

/** Ask the cheap model for a shorter program that keeps the finding; the oracle decides whether to accept it. */
async function proposeShorter(tool: Tool, info: RuleInfo, code: string, kind: FindingKind, observed: string): Promise<{ code?: string; cost: number }> {
  try {
    const r = await chat({
      model: MODELS.fast,
      messages: [
        { role: "system", content: "You shorten test programs. Return only the program text, no explanation, no code fences." },
        { role: "user", content: `Tool ${tool.id}, lint rule ${info.rule}. The tool's automatic fix changed this program's behavior (${kind}): ${observed.slice(0, 400)}

Rewrite the program to be as short as possible while keeping (1) the exact construct the rule rewrites, (2) the surrounding code that makes the rewrite change behavior, (3) the printed output that shows the difference. Keep it deterministic and self-contained. Do not rename identifiers. Program:

${code}` },
      ],
      maxTokens: 1200,
      temperature: 0.7, // Lightning ignores line budgets at low temperature; the oracle rejects bad proposals anyway
      tag: "minimize",
    });
    const text = r.text.trim().replace(/^```[a-z]*\n?|\n?```$/g, "").trim() + "\n";
    return { code: text.split("\n").length < code.trimEnd().split("\n").length ? text : undefined, cost: r.cost };
  } catch {
    return { cost: 0 };
  }
}

/** Reduce `code` while the evaluation still produces a finding of `kind`. */
export function minimize(tool: Tool, info: RuleInfo, dir: string, id: string, code: string, kind: FindingKind, unsafe: boolean, budget = 60): Promise<MinimizeResult> {
  return withLocalSandbox(() => minimizeImpl(tool, info, dir, id, code, kind, unsafe, budget));
}

async function minimizeImpl(tool: Tool, info: RuleInfo, dir: string, id: string, code: string, kind: FindingKind, unsafe: boolean, budget: number): Promise<MinimizeResult> {
  let lines = code.replace(/\n+$/, "").split("\n");
  const original = lines.length;
  let evaluations = 0;
  let last: ProgramResult | undefined;
  // Invariant: the reduced program must keep the same finding kind AND the same "before" exit status and
  // error line, so the reduction cannot turn a clean program into one that merely crashes earlier.
  const base = await evaluateProgram(tool, info, dir, { id: `${id}-min0`, title: "min", hazard: "", code, expectTrigger: true }, { unsafe });
  const baseBefore = base.before.run;
  const sameShape = (r: ProgramResult) =>
    !r.error && r.findings.some((f) => f.kind === kind) &&
    r.before.run.code === baseBefore.code && r.before.run.stderr1 === baseBefore.stderr1 && r.before.run.timedOut === baseBefore.timedOut;
  if (!sameShape(base)) return { code, lines: { before: original, after: original }, evaluations: 1, result: base, proposal: "skipped", cost: 0 };
  last = base;

  // Nemotron 3.5 Lightning proposes a shorter program; ddmin starts from it only if the oracle agrees.
  let proposal: MinimizeResult["proposal"] = "skipped";
  let cost = 0;
  if (process.env.FIXHUNT_MINIMIZE_PROPOSE !== "0") {
    const observed = base.findings.find((f) => f.kind === kind)?.detail ?? "";
    const prop = await proposeShorter(tool, info, code, kind, observed);
    cost += prop.cost;
    if (prop.code) {
      evaluations++;
      const pr = await evaluateProgram(tool, info, dir, { id: `${id}-prop`, title: "min", hazard: "", code: prop.code, expectTrigger: true }, { unsafe });
      if (sameShape(pr)) { lines = prop.code.replace(/\n+$/, "").split("\n"); last = pr; proposal = "accepted"; }
      else proposal = "rejected";
    }
  }

  const test = async (cand: string[]): Promise<boolean> => {
    if (evaluations >= budget) return false;
    evaluations++;
    const r = await evaluateProgram(tool, info, dir, { id: `${id}-min${evaluations}`, title: "min", hazard: "", code: cand.join("\n") + "\n", expectTrigger: true }, { unsafe });
    const ok = sameShape(r);
    if (ok) last = r;
    return ok;
  };

  // ddmin over line chunks
  let n = 2;
  while (lines.length >= 2 && evaluations < budget) {
    const chunk = Math.ceil(lines.length / n);
    let reduced = false;
    for (let i = 0; i < lines.length; i += chunk) {
      const complement = [...lines.slice(0, i), ...lines.slice(i + chunk)];
      if (complement.length === 0) continue;
      if (await test(complement)) {
        lines = complement;
        n = Math.max(n - 1, 2);
        reduced = true;
        break;
      }
    }
    if (!reduced) {
      if (n >= lines.length) break;
      n = Math.min(n * 2, lines.length);
    }
  }
  // final single-line pass, also tries blanking inner whitespace-only lines
  for (let i = lines.length - 1; i >= 0 && evaluations < budget; i--) {
    if (lines.length <= 1) break;
    const cand = [...lines.slice(0, i), ...lines.slice(i + 1)];
    if (await test(cand)) lines = cand;
  }
  return { code: lines.join("\n") + "\n", lines: { before: original, after: lines.length }, evaluations, result: last!, proposal, cost };
}
