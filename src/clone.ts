// Shallow clone of a public repository for a scan started from the dashboard. Hosts are allow-listed, the clone is
// depth 1 without tags, prompts are disabled, and the checkout is size-capped before anything is uploaded to a sandbox.
import { mkdtempSync, rmSync, realpathSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { exec } from "./sandbox";

const HOSTS = (process.env.FIXHUNT_CLONE_HOSTS ?? "github.com,gitlab.com,codeberg.org,bitbucket.org").split(",").map((s) => s.trim());
const MAX_MB = Number(process.env.FIXHUNT_MAX_ARCHIVE_MB ?? 50);

export function parseRepoUrl(u: string): { url: string; name: string } | undefined {
  const m = /^https:\/\/([\w.-]+)\/([\w.-]+)\/([\w.-]+?)(?:\.git)?\/?$/.exec(u.trim());
  if (!m || !HOSTS.includes(m[1]) || m[2].startsWith(".") || m[3].startsWith(".")) return undefined;
  return { url: `https://${m[1]}/${m[2]}/${m[3]}`, name: m[3] };
}

export async function cloneRepo(u: string, opts: { timeoutMs?: number } = {}): Promise<{ dir: string; url: string; name: string; head: string; mb: number }> {
  const r = parseRepoUrl(u);
  if (!r) throw new Error(`repository must be an https URL on ${HOSTS.join(", ")}`);
  const dir = mkdtempSync(join(tmpdir(), "fixhunt-clone-"));
  try {
    const c = await exec(["git", "clone", "--quiet", "--depth", "1", "--single-branch", "--no-tags", "--", r.url, "src"], { cwd: dir, timeoutMs: opts.timeoutMs ?? 120_000, env: { GIT_TERMINAL_PROMPT: "0", GIT_ASKPASS: "echo" } });
    if (c.code !== 0) throw new Error(c.timedOut ? "clone timed out" : `clone failed: ${c.stderr.trim().split("\n").pop()?.slice(0, 200) ?? "unknown error"}`);
    const src = join(dir, "src");
    const rev = await exec(["git", "rev-parse", "--short", "HEAD"], { cwd: src, timeoutMs: 30_000 });
    rmSync(join(src, ".git"), { recursive: true, force: true });
    // No symbolic links: a link out of the checkout would let a config reader or fixer reach the host
    await exec(["find", ".", "-type", "l", "-delete"], { cwd: src, timeoutMs: 30_000 });
    const du = await exec(["du", "-sm", "."], { cwd: src, timeoutMs: 30_000 });
    const mb = Number(du.stdout.split("\t")[0]) || 0;
    if (mb > MAX_MB) throw new Error(`checkout is ${mb} MB; the limit is ${MAX_MB} MB`);
    const head = rev.stdout.trim();
    return { dir: src, url: r.url, name: r.name, head, mb };
  } catch (e) {
    rmSync(dir, { recursive: true, force: true });
    throw e;
  }
}

export function removeClone(dir: string) { rmSync(join(dir, ".."), { recursive: true, force: true }); }

/** A directory inside a checkout, from a user-supplied relative path: no absolute paths, no `..`, must exist and stay inside the
 * checkout once symbolic links are resolved. Returns the normalized relative path. */
export function subdir(checkout: string, rel: string): { path: string; dir: string } | { error: string } {
  const norm = rel.trim().replace(/\\/g, "/");
  if (norm.startsWith("/")) return { error: "path must be relative to the repository root" };
  const parts = norm.split("/").filter((p) => p !== "" && p !== ".");
  if (!parts.length) return { path: "", dir: checkout };
  if (parts.some((p) => p === ".." || p.startsWith("\0"))) return { error: "path must be relative to the repository root" };
  const path = parts.join("/");
  let dir: string;
  try { dir = realpathSync(join(checkout, path)); } catch { return { error: `no directory "${path}" in the repository` }; }
  const root = realpathSync(checkout);
  if (dir !== root && !dir.startsWith(root + "/")) return { error: "path must stay inside the repository" };
  if (!statSync(dir).isDirectory()) return { error: `"${path}" is not a directory` };
  return { path, dir };
}
