// Unit tests for the model-free parts of a repository scan: hunk parsing, application and rendering (delta debugging works
// on these), output normalization, the observed-difference text and the build-break classification.
import { describe, expect, test } from "bun:test";
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { applyHunks, configDir, isBuildBreak, norm, observe, parseHunks, renderHunks, scrub } from "./scan";
import { loadTools } from "./tools/registry";

const DIFF = `diff -ruN base/src/a.py rule/src/a.py
--- base/src/a.py\t2026-10-23 00:00:00.000000000 -0400
+++ rule/src/a.py\t2026-10-23 00:00:01.000000000 -0400
@@ -1,4 +1,3 @@
 import os
-x = 1
-y = 2
+x, y = 1, 2
 print(x, y)
@@ -10,2 +9,3 @@
 def f():
+    pass
     return 1
diff -ruN base/src/b.py rule/src/b.py
--- base/src/b.py\t2026-10-23 00:00:00.000000000 -0400
+++ rule/src/b.py\t2026-10-23 00:00:01.000000000 -0400
@@ -1 +1 @@
-print("a")
+print("b")
`;

describe("parseHunks", () => {
  test("names files from the old side without the compared root, and keeps hunk counts", () => {
    const { hunks, binary, invalid } = parseHunks(DIFF);
    expect(invalid).toBe(false);
    expect(binary).toEqual([]);
    expect(hunks.map((h) => h.file)).toEqual(["src/a.py", "src/a.py", "src/b.py"]);
    expect(hunks[0]).toMatchObject({ oldStart: 1, oldLines: 4, newStart: 1, newLines: 3 });
    expect(hunks[1]).toMatchObject({ oldStart: 10, oldLines: 2, newStart: 9, newLines: 3 });
    expect(hunks[2]).toMatchObject({ oldStart: 1, oldLines: 1, newStart: 1, newLines: 1, lines: ['-print("a")', '+print("b")'] });
  });

  test("a content line that starts with --- stays inside its hunk", () => {
    const d = `--- a/x.md\n+++ b/x.md\n@@ -1,2 +1,2 @@\n-----\n+---\n title\n`;
    const { hunks, invalid } = parseHunks(d);
    expect(invalid).toBe(false);
    expect(hunks).toHaveLength(1);
    expect(hunks[0].lines).toEqual(["-----", "+---", " title"]);
  });

  test("a truncated hunk is flagged invalid", () => {
    const d = `--- a/x.py\n+++ b/x.py\n@@ -1,3 +1,3 @@\n-a\n+b\n`;
    expect(parseHunks(d).invalid).toBe(true);
  });

  test("binary files are listed, not parsed", () => {
    const d = `Binary files base/img.png and rule/img.png differ\n`;
    expect(parseHunks(d)).toEqual({ hunks: [], binary: ["img.png"], invalid: false });
  });

  test("a no-newline marker belongs to the hunk", () => {
    const d = `--- a/x.txt\n+++ b/x.txt\n@@ -1 +1 @@\n-a\n+b\n\\ No newline at end of file\n`;
    expect(parseHunks(d).hunks[0].lines).toEqual(["-a", "+b", "\\ No newline at end of file"]);
  });
});

describe("applyHunks", () => {
  const a = parseHunks(DIFF).hunks.filter((h) => h.file === "src/a.py");
  const base = "import os\nx = 1\ny = 2\nprint(x, y)\n5\n6\n7\n8\n9\ndef f():\n    return 1\n";

  test("applies every hunk of a file", () => {
    expect(applyHunks(base, a)).toBe("import os\nx, y = 1, 2\nprint(x, y)\n5\n6\n7\n8\n9\ndef f():\n    pass\n    return 1\n");
  });

  test("applies a subset, which is what delta debugging needs", () => {
    expect(applyHunks(base, [a[1]])).toBe("import os\nx = 1\ny = 2\nprint(x, y)\n5\n6\n7\n8\n9\ndef f():\n    pass\n    return 1\n");
  });

  test("rejects a hunk whose context does not match", () => {
    expect(applyHunks(base.replace("print(x, y)", "print(y)"), a)).toBeUndefined();
  });

  test("an empty file gains content without a phantom first line", () => {
    const h = parseHunks(`--- a/n.txt\n+++ b/n.txt\n@@ -0,0 +1 @@\n+x\n`).hunks;
    expect(applyHunks("", h)).toBe("x\n");
  });

  test("deleting everything yields the empty string, not a newline", () => {
    const h = parseHunks(`--- a/n.txt\n+++ b/n.txt\n@@ -1 +0,0 @@\n-abc\n`).hunks;
    expect(applyHunks("abc\n", h)).toBe("");
  });

  test("honours a no-newline marker on the new side", () => {
    const h = parseHunks(`--- a/n.txt\n+++ b/n.txt\n@@ -1 +1 @@\n-a\n+b\n\\ No newline at end of file\n`).hunks;
    expect(applyHunks("a\n", h)).toBe("b");
  });

  test("keeps a missing trailing newline when the hunk does not touch the end", () => {
    const h = parseHunks(`--- a/n.txt\n+++ b/n.txt\n@@ -1 +1 @@\n-a\n+b\n`).hunks;
    expect(applyHunks("a\nc", h)).toBe("b\nc");
  });
});

describe("renderHunks", () => {
  test("recomputes new-side starts for a subset and applies with git apply", async () => {
    const all = parseHunks(DIFF).hunks;
    const subset = [all[1], all[2]]; // skip the first hunk of a.py: the second one's new start must shift back by one
    const text = renderHunks(subset);
    expect(text).toContain("--- a/src/a.py\n+++ b/src/a.py\n@@ -10,2 +10,3 @@");
    expect(text).toContain("--- a/src/b.py\n+++ b/src/b.py\n@@ -1 +1 @@");
    const dir = mkdtempSync(join(tmpdir(), "fixhunt-test-"));
    mkdirSync(join(dir, "src"));
    writeFileSync(join(dir, "src/a.py"), "import os\nx = 1\ny = 2\nprint(x, y)\n5\n6\n7\n8\n9\ndef f():\n    return 1\n");
    writeFileSync(join(dir, "src/b.py"), 'print("a")\n');
    const p = Bun.spawn(["git", "apply", "-p1", "--whitespace=nowarn", "-"], { cwd: dir, stdin: Buffer.from(text), stdout: "pipe", stderr: "pipe" });
    expect(await p.exited).toBe(0);
    expect(readFileSync(join(dir, "src/a.py"), "utf8")).toBe("import os\nx = 1\ny = 2\nprint(x, y)\n5\n6\n7\n8\n9\ndef f():\n    pass\n    return 1\n");
    expect(readFileSync(join(dir, "src/b.py"), "utf8")).toBe('print("b")\n');
  });

  test("round-trips a parsed diff", () => {
    const hs = parseHunks(DIFF).hunks;
    const again = parseHunks(renderHunks(hs)).hunks;
    expect(again.map((h) => [h.file, h.oldStart, h.oldLines, h.newStart, h.newLines, h.lines])).toEqual(hs.map((h) => [h.file, h.oldStart, h.oldLines, h.newStart, h.newLines, h.lines]));
  });
});

describe("normalization", () => {
  test("scrubs timings, temp paths, addresses and positions", () => {
    expect(scrub("ran 3 tests in 0.012s at /tmp/abc.1 (0x7fff) file.py:12:3 duration_ms: 1.5")).toBe("ran 3 tests in Ns at /tmp/X (0xX) file.py:N duration_ms N");
  });

  test("two runs that differ only in noise normalize the same", () => {
    const a = { stdout: "ok 1 - t\n# duration_ms 12.3", stderr: "Ran 2 tests in 0.004s\n\nOK", code: 0, timedOut: false };
    const b = { stdout: "ok 1 - t\n# duration_ms 45.6", stderr: "Ran 2 tests in 0.011s\n\nOK", code: 0, timedOut: false };
    expect(norm(a)).toBe(norm(b));
  });

  test("observe names the lines on one side only and the exit change", () => {
    const b = { stdout: "a\nb\n", stderr: "", code: 0, timedOut: false };
    const a = { stdout: "a\nc\n", stderr: "boom", code: 1, timedOut: false };
    const o = observe(b, a);
    expect(o).toContain("stdout lines only before the fix:\n  b");
    expect(o).toContain("stdout lines only after the fix:\n  c");
    expect(o).toContain("exit 0 → 1");
    expect(o).toContain("stderr last line after: boom");
  });
});

describe("isBuildBreak", () => {
  const ok = { stdout: "", stderr: "", code: 0, timedOut: false };
  test("a compiler or import error after a passing run is a build break", () => {
    expect(isBuildBreak(ok, { stdout: "", stderr: "src/a.cpp:3:5: error: expected ';'", code: 1, timedOut: false })).toBe(true);
    expect(isBuildBreak(ok, { stdout: "", stderr: 'Traceback (most recent call last):\n  File "x.py", line 1\nSyntaxError: invalid syntax', code: 1, timedOut: false })).toBe(true);
    expect(isBuildBreak(ok, { stdout: "# SyntaxError: Unexpected token", stderr: "", code: 1, timedOut: false })).toBe(true); // node:test forwards stderr with "# "
  });
  test("a failing test that mentions an error class is not a build break", () => {
    expect(isBuildBreak(ok, { stdout: "not ok 1 - handles SyntaxError in input", stderr: "", code: 1, timedOut: false })).toBe(false);
    expect(isBuildBreak(ok, { stdout: "", stderr: "AssertionError: 1 != 2", code: 1, timedOut: false })).toBe(false);
  });
  test("needs a passing run before and a failing one after", () => {
    expect(isBuildBreak({ ...ok, code: 1 }, { stdout: "", stderr: "a.c:1:1: error: x", code: 1, timedOut: false })).toBe(false);
    expect(isBuildBreak(ok, { stdout: "", stderr: "a.c:1:1: error: x", code: 0, timedOut: false })).toBe(false);
  });
});

describe("configDir", () => {
  const ruff = loadTools().ruff;
  const root = mkdtempSync(join(tmpdir(), "fixhunt-cfg-"));
  mkdirSync(join(root, "pkg", "sub"), { recursive: true });
  writeFileSync(join(root, "pyproject.toml"), "[tool.ruff]\n");
  test("walks up from the scanned directory to the nearest configuration, bounded by the root", () => {
    expect(configDir(ruff, join(root, "pkg", "sub"), root)).toBe(root);
    writeFileSync(join(root, "pkg", "ruff.toml"), "");
    expect(configDir(ruff, join(root, "pkg", "sub"), root)).toBe(join(root, "pkg"));
    expect(configDir(ruff, join(root, "pkg", "sub"), join(root, "pkg", "sub"))).toBe(join(root, "pkg", "sub"));
  });
  test("without a root, the scanned directory is used as is", () => {
    expect(configDir(ruff, join(root, "pkg", "sub"))).toBe(join(root, "pkg", "sub"));
  });
});
