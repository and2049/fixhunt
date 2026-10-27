import { describe, expect, test } from "bun:test";
import { fixtureName, fixtureText, type Finding } from "./data";

const finding = (over: Partial<Finding["report"]> = {}, ext = "py"): Finding => ({
  run: { id: "2026-10-17T19-38-23-545Z-dfhv-ruff-FURB103", dir: "", tool: "ruff", ext, version: "ruff 0.17.1", rule: { rule: "FURB103", fixKind: "safe" } as any, cost: 0, summary: {}, reports: [], results: [], when: "" },
  report: {
    programId: "r1-p006", kind: "fix-changes-behavior", safeLabel: true, minimized: 'flag = False\nwith open("o.txt", "w") as f:\n    flag and f.write("x")\n', lines: { before: 3, after: 2 }, reportPath: "", duplicates: [],
    evidence: { diff: "", observed: "", before: { stdout: "", stderr1: "", code: 0, timedOut: false }, after: { stdout: "should not happen", stderr1: "", code: 0, timedOut: false }, fixed: "", commands: [], fired: 1, firedAfter: 0 },
    ...over,
  } as Finding["report"],
  result: {} as any, grade: "real", severity: "high", upstream: "none", rank: 1,
});

describe("fixtureText", () => {
  test("is a comment header followed by the minimized program, unchanged", () => {
    const t = fixtureText(finding());
    const [head, body] = t.split("\n\n");
    expect(head.split("\n").every((l) => l.startsWith("# "))).toBe(true);
    expect(head).toContain("ruff FURB103, ruff 0.17.1");
    expect(head).toContain("the fix labelled safe changes the program's output");
    expect(head).toContain("before the fix: no stdout, exit 0");
    expect(head).toContain('after the fix: stdout "should not happen", exit 0');
    expect(body).toBe('flag = False\nwith open("o.txt", "w") as f:\n    flag and f.write("x")\n');
  });
  test("keeps a hashbang on the first line", () => {
    const t = fixtureText(finding({ minimized: "#!/usr/bin/env node\nconsole.log(1)\n" }, "js"));
    expect(t.startsWith("#!/usr/bin/env node\n// fixhunt")).toBe(true);
    expect(t.endsWith("\n\nconsole.log(1)\n")).toBe(true);
  });
  test("uses the language's comment syntax", () => {
    expect(fixtureText(finding({}, "js")).startsWith("// fixhunt")).toBe(true);
    expect(fixtureText(finding({}, "cpp")).startsWith("// fixhunt")).toBe(true);
  });
  test("omits the after line when the fix left nothing to run", () => {
    const t = fixtureText(finding({ kind: "fix-breaks-syntax", evidence: { diff: "", observed: "", before: { stdout: "1", stderr1: "", code: 0, timedOut: false }, fixed: "", commands: [], fired: 1, firedAfter: 0 } }));
    expect(t).toContain("produces a program that does not parse");
    expect(t).not.toContain("after the fix:");
  });
});

describe("fixtureName", () => {
  test("is tool, rule and program id with safe characters only", () => {
    expect(fixtureName(finding())).toBe("ruff-FURB103-r1-p006.py");
    const f = finding({}, "js"); f.run.tool = "biome"; (f.run.rule as any).rule = "complexity/noUselessLoneBlockStatements";
    expect(fixtureName(f)).toBe("biome-complexity-noUselessLoneBlockStatements-r1-p006.js");
  });
});
