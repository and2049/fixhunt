// Tool registry: every *.json in tools/ (and in FIXHUNT_TOOLS, colon-separated extra directories) is a tool.
import { existsSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { loadSpec, type SpecTool } from "./spec";

let cache: Record<string, SpecTool> | undefined;

export function toolDirs(): string[] {
  const dirs = [resolve("tools"), ...(process.env.FIXHUNT_TOOLS ?? "").split(":").filter(Boolean).map((d) => resolve(d))];
  return dirs.filter((d) => existsSync(d));
}

export function loadTools(extraFiles: string[] = []): Record<string, SpecTool> {
  if (cache && !extraFiles.length) return cache;
  const tools: Record<string, SpecTool> = {};
  for (const dir of toolDirs()) for (const f of readdirSync(dir).filter((f) => f.endsWith(".json")).sort()) {
    try { const t = loadSpec(join(dir, f)); tools[t.id] = t; } catch (e) { console.error(`skipping tool spec ${join(dir, f)}: ${String((e as Error).message ?? e)}`); }
  }
  for (const f of extraFiles) { const t = loadSpec(f); tools[t.id] = t; }
  if (!extraFiles.length) cache = tools;
  return tools;
}

export function getTool(id: string, extraFiles: string[] = []): SpecTool {
  const tools = loadTools(extraFiles);
  const t = tools[id];
  if (!t) throw new Error(`unknown tool "${id}"; available: ${Object.keys(tools).join(", ") || "(none; add a spec to tools/)"}`);
  return t;
}
