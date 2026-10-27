// Stage 1: TARGET. Two model steps per rule:
//   analyze  — read the rule docs once, derive rule-specific hazards and the exact firing shapes
//   generate — write self-checking programs for a batch of hazards; later rounds get feedback
import { chatJson } from "./llm";
import { MODELS } from "./config";
import type { RuleInfo } from "./tools/types";

export type GenProgram = { id: string; title: string; hazard: string; code: string; expectTrigger: boolean };

export type RuleAnalysis = {
  summary: string;
  firingShapes: string[]; // concrete syntactic shapes that trigger the rule
  silentShapes: string[]; // near-misses that must not trigger
  fixDescription: string; // what the autofix rewrites, in the model's words
  hazards: string[]; // rule-specific ways the rewrite could change behavior or produce invalid code
};

export type Feedback = { silent: string[]; invalid: string[]; fixOk: string[] }; // short program descriptions from the previous round

// Generic seed hazards per language, appended to the rule-specific list.
export const HAZARDS: Record<string, string[]> = {
  js: [
    "var hoisting and re-declaration inside loops or after use",
    "function declarations inside blocks, switch cases, labeled statements",
    "getters, setters and Object.defineProperty side effects",
    "__proto__ keys, prototype access, Object.assign vs spread",
    "arguments object, function.length, default parameters, rest parameters",
    "this binding: arrow vs function, methods extracted from objects, call/apply/bind",
    "comments attached to the removed or moved code",
    "numeric/string coercion: + vs template literal, objects with toString/valueOf, Symbol, BigInt",
    "ASI and semicolon-less code, leading ( or [ on the next line",
    "regular expressions: escapes, unicode flag, lastIndex with the g flag",
    "sparse arrays, holes, Array(n) vs [n], array-likes",
    "label/break/continue control flow, finally blocks, early returns in nested blocks",
    "name collisions across scopes after a move (shadowing)",
    "temporal dead zone after code is hoisted or reordered",
    "strict vs sloppy mode semantics",
    "order of evaluation when expressions are merged, duplicated or deleted (side effects run twice or never)",
    "null/undefined distinction, optional chaining short-circuit, nullish vs falsy",
    "async/await ordering, generators and yield position",
    "class fields, static blocks, private names, super calls",
    "exceptions thrown inside the code the fix removes or rewrites",
  ],
  cpp: [
    "macros: the rewritten token comes from or spans a macro expansion, or a macro argument",
    "preprocessor conditionals (#if/#ifdef) inside or around the rewritten statement",
    "templates: dependent types, decltype/typeof-style expressions, requires clauses, NTTPs",
    "operator precedence and parentheses that look redundant but change grouping (casts, comma, ternary, sizeof)",
    "implicit conversions, overloaded operators and user-defined conversions with side effects",
    "evaluation order and side effects when expressions are merged, duplicated or deleted",
    "references vs values: lifetime of temporaries, dangling after a rewrite to auto or structured bindings",
    "const/volatile/noexcept/constexpr qualifiers dropped or added by the rewrite",
    "comments and trailing comments attached to the removed or moved tokens",
    "member functions vs free functions with the same name, ADL, namespaces and using-directives",
    "braces: single-statement bodies, dangling else, labels, case fall-through",
    "lambdas: captures, mutable, init-captures, default parameters",
    "integer promotion, signedness, overflow, narrowing in the rewritten expression",
    "iterators invalidated or consumed when a loop is rewritten to range-based for",
    "exceptions thrown inside the rewritten code, RAII order of destruction",
    "static/thread_local/inline storage and initialization order",
    "virtual dispatch, overrides and final after the rewrite",
    "string literal types, string_view vs std::string, char vs int in the rewritten code",
  ],
  py: [
    "mutable default arguments and aliasing after a rewrite",
    "evaluation order and side effects when expressions are merged, duplicated or deleted",
    "generators vs lists, iterators consumed once, lazy vs eager evaluation",
    "exceptions raised inside the rewritten code, finally/else clauses, exception chaining",
    "bytes vs str, encoding and newline handling, text vs binary modes",
    "file modes and truncation, partial writes, non-str data passed to write",
    "walrus, comprehensions scoping, late binding in closures and lambdas",
    "dict ordering, duplicate keys, __hash__/__eq__ overrides, sets",
    "keyword-only, positional-only, *args/**kwargs forwarding, defaults evaluated once",
    "comments and docstrings attached to the removed or moved code",
    "class attributes vs instance attributes, descriptors, properties with side effects",
    "truthiness of custom __bool__/__len__, None vs falsy, 'is' vs '=='",
    "string formatting edge cases: %, format, f-strings, repr vs str, nested quotes",
    "int/float/bool coercion, Decimal, division and rounding",
    "context managers that are not files, objects with write() but no close()",
    "shadowed builtins and names redefined later in the module",
    "star-imports, module-level side effects, __all__",
    "async def/await ordering, async generators",
    "type annotations evaluated at runtime, typing-only imports",
    "pathlib vs os.path behavior on relative paths, symlinks, missing files, bytes paths",
  ],
};

const ANALYSIS_SCHEMA = {
  type: "object",
  properties: {
    summary: { type: "string" },
    firing_shapes: { type: "array", items: { type: "string" } },
    silent_shapes: { type: "array", items: { type: "string" } },
    fix_description: { type: "string" },
    hazards: { type: "array", items: { type: "string" } },
  },
  required: ["summary", "firing_shapes", "silent_shapes", "fix_description", "hazards"],
};

const PROGRAMS_SCHEMA = {
  type: "object",
  properties: {
    programs: {
      type: "array",
      items: {
        type: "object",
        properties: {
          title: { type: "string" },
          hazard: { type: "string" },
          expect_trigger: { type: "boolean" },
          code: { type: "string" },
        },
        required: ["title", "hazard", "expect_trigger", "code"],
      },
    },
  },
  required: ["programs"],
};

export async function analyzeRule(info: RuleInfo, language: string): Promise<{ analysis: RuleAnalysis; cost: number }> {
  const sys = `You are an expert in ${langName(language)} semantics and in the implementation of linter autofixes. You reason precisely about what a rewrite preserves and what it does not.`;
  const user = `Tool: ${info.tool}. Rule: ${info.rule}. The tool labels the fix: ${info.fixKind}.

Rule documentation:
---
${info.docs.slice(0, 7000)}
---

Analyze this rule for autofix testing.
1. summary: one sentence on what the rule flags.
2. firing_shapes: 4-8 concrete ${langName(language)} code shapes (one line each, real code) on which the rule fires. Use the keyword/construct forms shown under the documentation's invalid examples.
3. silent_shapes: 3-5 near-miss shapes on which it must stay silent.
4. fix_description: what the autofix rewrites the code into, precisely.
5. hazards: 8-12 rule-specific ways this exact rewrite could change program behavior, break compilation/parsing, or move/drop comments. Each hazard is one sentence that names the construct and why the rewrite is not equivalent there. Think about scoping, hoisting, evaluation order, side effects, aliasing, types, mode/flags, comments, and interactions with surrounding code. Do not list generic advice.

Return JSON with keys summary, firing_shapes, silent_shapes, fix_description, hazards.`;
  const r = await chatJson<any>({
    model: MODELS.mid,
    messages: [{ role: "system", content: sys }, { role: "user", content: user }],
    schema: { name: "analysis", schema: ANALYSIS_SCHEMA },
    maxTokens: 4000,
    temperature: 0.4,
    tag: "analyze",
  });
  const a = r.value;
  const analysis: RuleAnalysis = {
    summary: String(a.summary ?? ""),
    firingShapes: strs(a.firing_shapes),
    silentShapes: strs(a.silent_shapes),
    fixDescription: String(a.fix_description ?? ""),
    hazards: strs(a.hazards),
  };
  return { analysis, cost: r.cost };
}

export async function generatePrograms(
  info: RuleInfo,
  analysis: RuleAnalysis,
  opts: { n: number; language: string; runner: string; seed?: number; feedback?: Feedback; model?: string },
): Promise<{ programs: GenProgram[]; cost: number }> {
  const pool = [...analysis.hazards, ...(HAZARDS[opts.language] ?? [])];
  const picked = pick(pool, Math.min(opts.n, pool.length), opts.seed ?? Date.now());
  const sys = `You are an expert in ${langName(opts.language)} semantics and in linter autofix bugs. You write small, deterministic, self-checking programs that sit on the semantic edge cases of one lint rule, to test whether the rule's automatic fix preserves program behavior. You write ordinary application code: the program never mentions linting, rules, fixes, "before" or "after".`;
  const fb = opts.feedback
    ? `
Feedback from the previous round:
${opts.feedback.silent.length ? `- These programs did NOT trigger the rule although they were meant to; the rule only fires on the firing shapes below, so use those shapes literally:\n${opts.feedback.silent.map((s) => "  * " + s).join("\n")}` : ""}
${opts.feedback.invalid.length ? `- These programs failed to parse or were not deterministic; write valid, deterministic code:\n${opts.feedback.invalid.map((s) => "  * " + s).join("\n")}` : ""}
${opts.feedback.fixOk.length ? `- These programs triggered the rule and the fix preserved behavior; do not repeat them, push harder on the hazards:\n${opts.feedback.fixOk.map((s) => "  * " + s).join("\n")}` : ""}
`
    : "";
  const user = `Tool: ${info.tool}. Rule: ${info.rule} — ${analysis.summary}
The fix rewrites: ${analysis.fixDescription}

The rule fires on these shapes (use them literally, adapted to the hazard):
${analysis.firingShapes.map((s) => "  " + s).join("\n")}
It stays silent on:
${analysis.silentShapes.map((s) => "  " + s).join("\n")}
${fb}
Write ${opts.n} programs, one per hazard below, in order:
${picked.map((h, i) => `${i + 1}. ${h}`).join("\n")}

Requirements for every program:
- Self-contained ${langName(opts.language)}, runnable with "${opts.runner}". No imports beyond the standard library, no network, no randomness, no timers, no clock, no environment or argv. ${opts.language === "py" ? "Files may be created only in the current directory and must be removed at the end." : "No filesystem access."}
- Deterministic output: print a short trace of the values that matter, including the results of the code the rule would rewrite. Catch expected exceptions and print their type and message.
- At most 30 lines. Only comments that are part of the hazard.
- The trace must depend on the rewritten code so that a behavior change shows up in the output.
- Contain one or two spots where the rule fires (expect_trigger=true), unless the hazard is about a near-miss (expect_trigger=false).
- Make the construct the rule rewrites interact with the surrounding code: loops that re-enter it, later re-declarations, closures capturing it, side effects in its arguments, comments attached to it.

Return JSON: {"programs":[{"title":"...", "hazard":"...", "expect_trigger":true, "code":"..."}]}`;
  const r = await chatJson<{ programs: Array<{ title: string; hazard: string; expect_trigger: boolean; code: string }> }>({
    model: opts.model ?? MODELS.gen,
    messages: [{ role: "system", content: sys }, { role: "user", content: user }],
    // json_schema mode truncates Nemotron 3.5 Lightning to a single array item; plain JSON parses fine
    schema: process.env.FIXHUNT_GEN_SCHEMA === "1" ? { name: "programs", schema: PROGRAMS_SCHEMA } : undefined,
    maxTokens: 14_000,
    temperature: 0.9,
    tag: "generate",
  });
  const programs = (r.value.programs ?? [])
    .filter((p) => p && typeof p.code === "string" && p.code.trim())
    .map((p, i) => ({
      id: `p${String(i + 1).padStart(3, "0")}`,
      title: String(p.title ?? "").slice(0, 120),
      hazard: String(p.hazard ?? picked[i] ?? "").slice(0, 200),
      code: unescapeCode(p.code).replace(/\r\n/g, "\n").trimEnd() + "\n",
      expectTrigger: p.expect_trigger !== false,
    }));
  return { programs, cost: r.cost };
}

/** Cheap static screens for generated programs; returns a reason if the program must be rejected. */
export function screenProgram(language: string, code: string): string | undefined {
  const bad: Array<[RegExp, string]> = language === "js"
    ? [
        [/\bMath\.random\b/, "uses Math.random"],
        [/\b(?:Date\.now|new Date)\b/, "uses the clock"],
        [/\b(?:setTimeout|setInterval|setImmediate|queueMicrotask)\b/, "uses timers"],
        [/\b(?:require|import)\s*\(?\s*['"]/, "imports a module"],
        [/\bprocess\.(?:argv|env|stdin)\b/, "reads process state"],
        [/^\s*print\s*\(/m, "calls print() (not JavaScript)"],
      ]
    : language === "cpp"
      ? [
          [/\b(?:rand|srand|random_device|std::chrono|time\(|clock\()/, "uses randomness or the clock"],
          [/\b(?:std::thread|pthread|fork\(|system\(|popen\(|getenv\()/, "uses threads, processes or the environment"],
          [/\b(?:std::cin|getchar|scanf|argv)\b/, "reads input"],
          [/\b(?:std::ifstream|std::ofstream|fopen|std::filesystem)\b/, "uses the filesystem"],
        ]
    : language === "py"
      ? [
          [/\bimport\s+random\b|\bfrom\s+random\b/, "uses random"],
          [/\b(?:time\.time|time\.perf_counter|datetime\.now|datetime\.today)\b/, "uses the clock"],
          [/\binput\s*\(/, "reads stdin"],
          [/\bsys\.argv\b|\bos\.environ\b/, "reads process state"],
          [/\b(?:subprocess|socket|urllib|requests|http\.client)\b/, "uses network or subprocess"],
        ]
      : [];
  for (const [re, why] of bad) if (re.test(code)) return why;
  return undefined;
}

/** Models sometimes double-escape newlines inside the JSON string; recover when the code has no real line breaks. */
function unescapeCode(code: string): string {
  if (code.includes("\n") || !code.includes("\\n")) return code;
  return code.replace(/\\n/g, "\n").replace(/\\t/g, "\t").replace(/\\"/g, '"');
}

function strs(x: unknown): string[] {
  return Array.isArray(x) ? x.map((s) => String(s)).filter(Boolean) : [];
}

function langName(l: string) {
  return l === "js" ? "JavaScript" : l === "py" ? "Python" : l === "cpp" ? "C++ (C++20, single translation unit, standard library only, prints with std::printf or std::cout, returns 0)" : l;
}

function pick<T>(arr: T[], n: number, seed: number): T[] {
  const a = [...arr];
  let s = seed >>> 0 || 1;
  for (let i = a.length - 1; i > 0; i--) {
    s = (s * 1664525 + 1013904223) >>> 0;
    const j = s % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a.slice(0, n);
}
