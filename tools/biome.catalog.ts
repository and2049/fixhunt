// Catalog helper for the Biome spec: lists every lint rule with its fix label and example languages.
// Reads the rule names from Biome's configuration schema and asks `biome explain` about each one.
import { readFileSync } from "node:fs";
const BIOME = (process.env.FIXHUNT_BIOME ?? "bunx --bun @biomejs/biome").split(/\s+/);
const schema = JSON.parse(readFileSync("node_modules/@biomejs/biome/configuration_schema.json", "utf8"));
const defs = schema.definitions ?? schema.$defs ?? {};
// Recommended status comes from Biome's published rule metadata (not in the package); absent when offline
const recommended = new Map<string, boolean>();
try {
  const meta: any = await (await fetch("https://biomejs.dev/metadata/rules.json", { signal: AbortSignal.timeout(20_000) })).json();
  for (const lang of Object.values(meta.lints?.languages ?? {}) as any[]) for (const group of Object.values(lang) as any[]) for (const [name, r] of Object.entries(group) as any[]) if (r?.recommended) recommended.set(name, true);
} catch {}
const out: Array<{ rule: string; name: string; fixKind: string; languages: string[]; recommended?: boolean }> = [];
for (const g of ["A11y", "Complexity", "Correctness", "Nursery", "Performance", "Security", "Style", "Suspicious"]) {
  for (const name of Object.keys(defs[g]?.properties ?? {}).filter((k) => k !== "recommended" && k !== "all")) {
    const p = Bun.spawnSync([...BIOME, "explain", name], { stdout: "pipe", stderr: "pipe" });
    const text = new TextDecoder().decode(p.stdout);
    const rule = /Diagnostic category:\s*lint\/([\w/-]+)/.exec(text)?.[1] ?? `${g.toLowerCase()}/${name}`;
    const fix = /^- Fix:\s*(\w+)/m.exec(text)?.[1]?.toLowerCase();
    const languages = [...new Set([...text.matchAll(/```(\w+)/g)].map((m) => m[1].toLowerCase().replace(/^(js|jsx|javascript)$/, "js").replace(/^(ts|tsx|typescript)$/, "ts")))];
    out.push({ rule, name, fixKind: fix === "safe" ? "safe" : fix === "unsafe" ? "unsafe" : p.exitCode === 0 ? "none" : "unknown", languages, recommended: recommended.size ? recommended.has(name) : undefined });
  }
}
console.log(JSON.stringify(out));
