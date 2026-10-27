import { describe, expect, test } from "bun:test";
import { mkdtempSync, mkdirSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { parseRepoUrl, subdir } from "./clone";

describe("parseRepoUrl", () => {
  test("accepts https URLs on the allow-listed hosts, with or without .git", () => {
    expect(parseRepoUrl("https://github.com/and2049/fixhunt")).toEqual({ url: "https://github.com/and2049/fixhunt", name: "fixhunt" });
    expect(parseRepoUrl("https://github.com/and2049/fixhunt.git/")).toEqual({ url: "https://github.com/and2049/fixhunt", name: "fixhunt" });
    expect(parseRepoUrl("  https://gitlab.com/a/b ")).toEqual({ url: "https://gitlab.com/a/b", name: "b" });
  });
  test("rejects other hosts, schemes, dot-prefixed names and extra path segments", () => {
    for (const u of ["http://github.com/a/b", "https://example.com/a/b", "https://github.com/.a/b", "https://github.com/a/b/c", "git@github.com:a/b.git", ""]) expect(parseRepoUrl(u)).toBeUndefined();
  });
});

describe("subdir", () => {
  const root = mkdtempSync(join(tmpdir(), "fixhunt-clone-"));
  mkdirSync(join(root, "demo", "repo"), { recursive: true });
  writeFileSync(join(root, "demo", "file.txt"), "x");
  const outside = mkdtempSync(join(tmpdir(), "fixhunt-outside-"));
  symlinkSync(outside, join(root, "escape"));

  test("empty path is the checkout itself", () => {
    expect(subdir(root, "")).toEqual({ path: "", dir: root });
    expect(subdir(root, " ./ ")).toEqual({ path: "", dir: root });
  });
  test("a nested directory is normalized", () => {
    expect(subdir(root, "demo//repo/")).toMatchObject({ path: "demo/repo" });
    expect(subdir(root, "./demo/./repo")).toMatchObject({ path: "demo/repo" });
  });
  test("rejects parent references, files, missing directories and symlink escapes", () => {
    expect(subdir(root, "../x")).toHaveProperty("error");
    expect(subdir(root, "/demo")).toHaveProperty("error");
    expect(subdir(root, "/")).toHaveProperty("error");
    expect(subdir(root, "demo/../../x")).toHaveProperty("error");
    expect(subdir(root, "demo/file.txt")).toHaveProperty("error");
    expect(subdir(root, "nope")).toHaveProperty("error");
    expect(subdir(root, "escape")).toHaveProperty("error");
  });
});
