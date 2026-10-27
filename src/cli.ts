import { hunt } from "./hunt";
import { checkFile } from "./check";
import { exportSite } from "./web/export";
import { startServer } from "./server";
import { sweep } from "./sweep";
import { refreshEvidence, reprocess } from "./reprocess";
import { triageMarkdown } from "./triage";
import { judgeEval } from "./judgeeval";
import { getTool, loadTools } from "./tools/registry";
import { catalogFor } from "./catalog";
import { scan, treeChangedSince } from "./scan";
import { riskCheck } from "./known";
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";

const extraSpecs = process.argv.flatMap((a, i) => (a === "--tool-file" && process.argv[i + 1] ? [process.argv[i + 1]] : []));
const TOOLS = loadTools(extraSpecs);

function arg(name: string, def?: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  if (i >= 0) { const v = process.argv[i + 1]; return v === undefined || v.startsWith("--") ? def : v; }
  return def;
}
/** Boolean switch: present or not; never consumes the next argument. */
const flag = (name: string) => process.argv.includes(`--${name}`);

const cmd = process.argv[2];
if (cmd === "reprocess") {
  await reprocess(TOOLS as any, { only: arg("only"), force: flag("force") });
  process.exit(0);
}
if (cmd === "refresh") {
  await refreshEvidence(TOOLS as any, { only: arg("only"), force: flag("force") });
  process.exit(0);
}
if (cmd === "judge-eval") {
  await judgeEval({ stored: flag("stored"), limit: arg("limit") ? Number(arg("limit")) : undefined, only: arg("only"), out: arg("out") });
  process.exit(0);
}
if (cmd === "triage") {
  const md = triageMarkdown(arg("tool"));
  const out = arg("out");
  if (out) { await Bun.write(out, md); console.log(`wrote ${out}`); } else console.log(md);
  process.exit(0);
}
if (cmd === "render") {
  console.log(exportSite(arg("out")));
  process.exit(0);
}
if (cmd === "serve") {
  startServer(Number(arg("port", "8731")), TOOLS, arg("host"));
  await new Promise(() => {});
}
if (cmd === "tools") {
  for (const t of Object.values(TOOLS)) console.log(`${t.id}\t${t.language}\t${t.spec.repo ?? "-"}\t${t.source}`);
  process.exit(0);
}
if (cmd !== "hunt" && cmd !== "check" && cmd !== "sweep" && cmd !== "catalog" && cmd !== "scan" && cmd !== "risk" && cmd !== "apply") {
  console.log(`usage: bun src/cli.ts hunt --tool biome --rule <group/rule|rule> [--n 8] [--rounds 1] [--unsafe] [--seed 1]\n       bun src/cli.ts check --tool biome --rule <rule> --file prog.js [--unsafe] [--report]\n       bun src/cli.ts sweep --tool biome [--n 8] [--rounds 2] [--limit k] [--only regex] [--fresh]\n       bun src/cli.ts reprocess [--only substr] [--force]   # re-run minimize/judge/dedup/report on finished runs\n       bun src/cli.ts triage [--tool t] [--out docs/triage.md]   # findings table, real-graded first\n       bun src/cli.ts serve [--port 8731] [--host 127.0.0.1]   # dashboard with live hunts (FIXHUNT_TOKEN guards POSTs)\n       bun src/cli.ts render [--out runs/site]   # static export of the dashboard\n       bun src/cli.ts refresh [--only substr] [--force]   # model-free: recompute finding evidence\n       bun src/cli.ts scan --tool ruff --dir ~/proj --run "pytest -q" [--rules A,B] [--limit k] [--image img] [--no-net] [--timeout s] [--no-minimize] [--no-judge] [--no-upstream] [--no-combine]   # a real project: which fixes change its tests' outcome\n       bun src/cli.ts apply --tool ruff --dir ~/proj --run "pytest -q" [scan options] [--force]   # scan, then apply the fixes that passed to the working tree\n       bun src/cli.ts risk --tool ruff --dir ~/proj   # which enabled rules already have a verified finding (no sandbox, no model)\n       bun src/cli.ts tools   # list tool specs (tools/*.json, $FIXHUNT_TOOLS, --tool-file f.json)\n       bun src/cli.ts catalog --tool <id>   # rebuild data/<id>-rules.json from the spec's catalog command`);
  process.exit(cmd ? 1 : 0);
}
const toolId = arg("tool") ?? Object.keys(TOOLS)[0];
if (!toolId) { console.error("no tools: add a spec to tools/ or pass --tool-file"); process.exit(1); }
const tool = getTool(toolId, extraSpecs);
if (cmd === "catalog") {
  const rules = await catalogFor(tool, true);
  console.log(`${tool.id}: ${rules.length} rules written to data/${tool.id}-rules.json`);
  process.exit(0);
}
if (cmd === "risk") {
  const dir = arg("dir") ?? ".";
  const r = riskCheck(tool, dir, await catalogFor(tool).catch(() => []));
  console.log(r.enabled !== undefined ? `${tool.id}: ${r.enabled} rules enabled by ${r.file ?? "the defaults"}` : `${tool.id}: ${r.note}`);
  if (!r.known.length) console.log("  no enabled rule has a finding in the bank");
  for (const k of r.known) console.log(`  ${k.rule}\t${k.fixKind}\t${k.findings} finding(s)\t${k.grade}/${k.severity}${k.urls.length ? `\t${k.urls.map((u) => `${u.relation} ${u.url}`).join(", ")}` : ""}`);
  if (r.notEnabled) console.log(`  ${r.notEnabled} known-risk rule(s) of ${tool.id} are not enabled here`);
  process.exit(0);
}
if (cmd === "scan" || cmd === "apply") {
  const dir = arg("dir") ?? (cmd === "apply" ? "." : undefined); const run = arg("run");
  if (!dir || !run) { console.error(`${cmd} needs --dir <project> and --run "<command>" (e.g. --run "pytest -q")`); process.exit(1); }
  const rules = arg("rules")?.split(",").map((r) => r.trim()).filter(Boolean);
  const res = await scan({ tool, dir, run, rules, unsafe: flag("unsafe"), limit: arg("limit") ? Number(arg("limit")) : undefined, image: arg("image"), net: !flag("no-net"), timeoutMs: arg("timeout") ? Number(arg("timeout")) * 1000 : undefined, exclude: arg("exclude")?.split(","), upstream: flag("no-upstream") ? false : undefined, minimize: flag("no-minimize") ? false : undefined, judge: flag("no-judge") ? false : undefined, combine: cmd === "apply" ? true : flag("no-combine") ? false : undefined });
  if (cmd === "apply") {
    if (!res.combined || !res.combined.files) { console.log("nothing to apply: no fix changed files without changing the outcome"); process.exit(0); }
    if (!res.combined.verified && !flag("force")) { console.log("not applied: the accepted fixes did not verify together (see above); apply one rule at a time, or --force"); process.exit(1); }
    if (!res.combined.patch) { console.log("not applied: no patch was published for this scan (see above)"); process.exit(1); }
    const moved = treeChangedSince(dir, res.out, arg("exclude")?.split(",") ?? []);
    if (moved.length) { console.log(`not applied: the working tree changed during the scan (${moved.slice(0, 5).join(", ")}${moved.length > 5 ? ", …" : ""}); the verified result would not match it. Run again.`); process.exit(1); }
    // git apply resolves the patch's paths relative to the current directory, inside a repository or not
    const p = Bun.spawn(["git", "apply", "-p1", "--whitespace=nowarn", "-"], { cwd: resolve(dir), stdin: readFileSync(join(res.out, "accepted.patch")), stdout: "pipe", stderr: "pipe" });
    const err = await new Response(p.stderr).text();
    if ((await p.exited) !== 0) { console.error(`git apply failed:\n${err}`); process.exit(1); }
    console.log(`applied ${res.combined.rules.length} rule(s) to ${res.combined.files} file(s) in ${resolve(dir)}; review with git diff`);
  }
  process.exit(0);
}
if (cmd === "sweep") {
  const only = arg("only");
  await sweep({ tool, n: Number(arg("n", "8")), rounds: Number(arg("rounds", "2")), unsafe: flag("unsafe"), limit: arg("limit") ? Number(arg("limit")) : undefined, only: only ? new RegExp(only) : undefined, resume: !flag("fresh") });
  process.exit(0);
}
const rule = arg("rule");
if (!rule) { console.error("--rule is required"); process.exit(1); }
if (cmd === "check") {
  const file = arg("file");
  if (!file) { console.error("--file is required"); process.exit(1); }
  await checkFile(tool, rule, file, flag("unsafe"), flag("report"));
  process.exit(0);
}
await hunt({ tool, rule, n: Number(arg("n", "8")), rounds: Number(arg("rounds", "1")), unsafe: flag("unsafe"), seed: Number(arg("seed", "1")), model: arg("model"), report: !flag("no-report") });
