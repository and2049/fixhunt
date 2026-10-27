// Rule lookup helper for the ESLint spec: prints the fixability label and metadata of one built-in rule.
const { builtinRules } = await import("eslint/use-at-your-own-risk");
const id = process.argv[2];
const r: any = builtinRules.get(id);
if (!r) { console.error(`unknown ESLint rule ${id}`); process.exit(1); }
console.log(`Rule: ${id}\nFixable: ${r.meta?.fixable ?? "no"}\nType: ${r.meta?.type ?? "?"}\nDeprecated: ${r.meta?.deprecated ? "yes" : "no"}\nDescription: ${r.meta?.docs?.description ?? ""}\nDocs: ${r.meta?.docs?.url ?? ""}`);
