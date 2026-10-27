// Stage 6: JUDGE. Ultra grades each oracle-backed finding against the rule documentation. Advisory only:
// the oracle decided that behavior changed; the judge decides whether anyone should care.
import { chatJson } from "./llm";
import { MODELS } from "./config";
import type { Snap } from "./oracles";

export type Verdict = {
  grade: "real" | "intended-change" | "introspection-only" | "program-bug" | "unclear";
  severity: "high" | "medium" | "low";
  why: string;
  docsQuote?: string;
  differenceSource?: string;
};

const INTROSPECTION: Array<[RegExp, string]> = [
  [/\.source\b/, "RegExp.prototype.source"], [/\.stack\b/, "error stack text"], [/\.toString\(\)/, "toString of code"], [/Function\.prototype\.toString/, "function source"],
  [/\bnew Error\([^)]*\)\.stack|\.lineNumber\b|\bcolumnNumber\b/, "stack positions"],
  [/inspect\.getsource|inspect\.getsourcelines|\bco_firstlineno\b|\b__code__\b|\blinecache\b|sys\._getframe|\btraceback\b|\.lineno\b|\btb_lineno\b/, "python source/line introspection"],
  [/warnings\.|SyntaxWarning|DeprecationWarning/, "warning text"], [/\bast\.(parse|dump|unparse)\b|\bdis\.dis\b|\bcompile\(/, "program inspects its own AST/bytecode"],
];
const ENVIRONMENT: Array<[RegExp, string]> = [
  [/__dirname|__filename|\brequire\(|module\.exports|import\.meta/, "CommonJS/ESM module environment"], [/process\.(env|argv|platform|version)/, "process environment"],
  [/os\.environ|sys\.argv|sys\.version|platform\./, "python environment"], [/\bimport\s+(vue|react|lodash|numpy|pandas|requests)\b|from\s+(vue|react|numpy|pandas)\s+import/, "third-party import"],
];

function hints(code: string, before?: Snap): string[] {
  const out: string[] = [];
  for (const [re, label] of INTROSPECTION) if (re.test(code)) out.push(`program reads ${label}`);
  for (const [re, label] of ENVIRONMENT) if (re.test(code)) out.push(`program depends on ${label}`);
  if (before && !before.timedOut && before.code !== 0) out.push(`the program already exited with status ${before.code} BEFORE the fix (${before.stderr1 || "no stderr"})`);
  return out;
}

const SYSTEM = `You review candidate bugs in linter autofixes. A program was linted, the tool's automatic fix was applied, and a model-free oracle observed that the program's behavior changed (different stdout, exit status or error) or that the fixed file no longer parses. The oracle is never wrong about the difference. Your job is to classify WHY it differs, using the rule documentation.

Grades, in the order you must consider them:
1. "program-bug": the comparison is meaningless. Either the program already failed before the fix for a reason unrelated to the rewrite, or the difference comes from the execution environment rather than the rewrite: module system (CommonJS vs ES modules, __dirname vs import.meta), a missing third-party package, platform or interpreter specifics, undefined behavior, nondeterminism.
2. "introspection-only": the only thing that differs is text that mirrors the rewritten source itself: RegExp.prototype.source or toString() of the rewritten literal, Function.prototype.toString, error stack line/column numbers, inspect.getsource, co_firstlineno, warning messages that quote the source, comments. Any rewrite changes these; they are not behavior.
3. "intended-change": the difference is exactly the semantic change the rule exists to make, as stated or clearly implied by the documentation. Examples: a rule that rewrites 'x is 5' to 'x == 5' because identity comparison with a literal is always a mistake (so equality instead of identity is the point), a rule that replaces a deprecated alias with its replacement (so the deprecation warning disappears and the replacement's behavior applies), a rule that turns '\\d' in a normal string into a raw string (so the SyntaxWarning disappears). The program only demonstrates that the rule did what it documents, even if the program depended on the old behavior. Not a bug in the fix.
4. "real": none of the above. The documentation presents the rewrite as equivalent (or says nothing about this construct), the construct is plausible in ordinary code, and a user who applies the fix gets different runtime behavior or a file that no longer parses. The fix should not be labelled safe for this construct, or should not be offered.
5. "unclear": the evidence does not let you decide.

Severity: high = silent wrong results, data loss or a crash in plausible code; medium = needs an unusual but legal construct, or an exception where the program previously succeeded; low = contrived construct.

Reason from the diff, the two outputs and the documentation. The hints are computed mechanically from the program text; weigh them, do not treat them as the answer. Return JSON:
{"docs_quote": "<up to 25 words from the documentation that describe the rewrite, or 'none'>", "difference_source": "runtime-semantics" | "source-text-introspection" | "environment" | "pre-existing-failure", "grade": "...", "severity": "...", "why": "two or three sentences naming the construct and the reason"}`;

const FEW_SHOT = `Worked examples (abbreviated):
- ruff F632 rewrites 'x is []' to 'x == []'; output changes from False to True. Docs: "comparisons to literals using is always evaluate to False". grade: intended-change.
- Biome noAdjacentSpacesInRegex rewrites /a  b/ to /a {2}b/; the program prints re.source. grade: introspection-only.
- Biome noGlobalDirnameFilename rewrites __dirname to import.meta.dirname; the program runs as CommonJS and now throws. grade: program-bug (environment).
- ruff FURB103 rewrites 'flag and f.write(x)' inside 'with open(p, "w")' to 'Path(p).write_text(x)'; the guard is gone, the file is written when flag is False. Docs present the rewrite as equivalent. grade: real, high.
- Biome noUselessElse hoists 'let x' out of an else block into a scope that already declares x; the file no longer parses. grade: real, high.
- Biome noPrototypeBuiltins rewrites obj.hasOwnProperty(k) to Object.hasOwn(obj, k); the program gave obj its own hasOwnProperty property. The docs say the rule exists because the method can be shadowed or missing, so bypassing it is the point. grade: intended-change.
- Biome useNumberNamespace rewrites parseInt(x) to Number.parseInt(x) inside a function whose parameter is named Number. The docs say nothing about a shadowed Number; the fix assumes the global. grade: real, medium.
- A program whose "before" run already exits non-zero with an error unrelated to the rewrite, and whose "after" run differs only because that failure moved or disappeared. grade: program-bug.`;

export async function judgeFinding(inp: { tool: string; rule: string; fixKind: string; kind: string; observed: string; repro: string; diff: string; docs?: string; before?: Snap; after?: Snap }): Promise<{ verdict: Verdict; cost: number }> {
  const h = hints(inp.repro, inp.before);
  const r = await chatJson<{ docs_quote?: string; difference_source?: string; grade: string; severity: string; why: string }>({
    model: MODELS.judge,
    messages: [
      { role: "system", content: SYSTEM + "\n\n" + FEW_SHOT },
      { role: "user", content: `Tool ${inp.tool}, rule ${inp.rule}, fix labelled ${inp.fixKind}. Oracle: ${inp.kind}.\n\nRule documentation:\n${(inp.docs ?? "(none)").slice(0, 3500)}\n\nProgram (before the fix):\n${inp.repro}\n\nDiff applied by the fix:\n${inp.diff}\n\nObserved:\n${inp.observed}\n\nMechanical hints: ${h.length ? h.join("; ") : "none"}` },
    ],
    maxTokens: 900,
    temperature: 0.1,
    tag: "judge",
  });
  const g = String(r.value.grade ?? "unclear");
  const sv = String(r.value.severity ?? "low");
  return {
    verdict: {
      grade: (["real", "intended-change", "introspection-only", "program-bug", "unclear"].includes(g) ? g : "unclear") as Verdict["grade"],
      severity: (["high", "medium", "low"].includes(sv) ? sv : "low") as Verdict["severity"],
      why: String(r.value.why ?? ""),
      docsQuote: r.value.docs_quote ? String(r.value.docs_quote) : undefined,
      differenceSource: r.value.difference_source ? String(r.value.difference_source) : undefined,
    },
    cost: r.cost,
  };
}
