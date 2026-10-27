import { describe, expect, test } from "bun:test";
import { loadTools } from "./registry";

const tools = loadTools();

describe("shipped tool specs", () => {
  test("ruff, biome, eslint and clang-tidy load with a language and extension", () => {
    for (const id of ["ruff", "biome", "eslint", "clang-tidy"]) {
      expect(tools[id]).toBeDefined();
      expect(tools[id].language).toMatch(/^(py|js|cpp)$/);
      expect(tools[id].ext).toMatch(/^\w+$/);
    }
  });

  test("repro commands are run, fix, run, naming the rule and the file token as given (callers shell-quote it)", () => {
    for (const t of Object.values(tools)) {
      const lines = t.reproCommands("some-rule", `'my prog.${t.ext}'`, false);
      expect(lines.length).toBeGreaterThanOrEqual(3);
      expect(lines[1]).toContain("some-rule");
      for (const l of lines) expect(l).toContain(`'my prog.${t.ext}'`);
    }
  });

  test("unsafe repro commands add the tool's unsafe flag only when the spec has one", () => {
    const ruff = tools.ruff.reproCommands("FURB103", "p.py", true).join("\n");
    expect(ruff).toContain("--unsafe-fixes");
    const safe = tools.ruff.reproCommands("FURB103", "p.py", false).join("\n");
    expect(safe).not.toContain("--unsafe-fixes");
  });
});
