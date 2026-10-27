// Catalog helper for the ESLint spec: built-in rules with their fixability. ESLint has no safe/unsafe label;
// its rule authoring guide requires autofixes to preserve program behavior, so a fixable rule counts as "safe".
const { builtinRules } = await import("eslint/use-at-your-own-risk");
const out = [...builtinRules.entries()].map(([rule, r]: [string, any]) => ({
  rule, fixKind: r.meta?.fixable ? "safe" : "none", note: r.meta?.fixable ? `${r.meta.fixable} fix` : "no fix", deprecated: !!r.meta?.deprecated, url: r.meta?.docs?.url ?? "",
}));
console.log(JSON.stringify(out));
