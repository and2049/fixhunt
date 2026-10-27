// Catalog helper for the clang-tidy spec: every check the installed binary knows. clang-tidy does not label its
// fixes, so each check is "unknown": scans take explicit rule ids, or every check with --unsafe.
const bin = process.env.CLANG_TIDY || ["clang-tidy", "clang-tidy-21", "clang-tidy-20", "clang-tidy-19", "clang-tidy-18"].find((c) => Bun.which(c)) || "clang-tidy";
const p = Bun.spawnSync([bin, "--list-checks", "-checks=*"]);
if (p.exitCode !== 0) { console.error(p.stderr.toString()); process.exit(1); }
const out = p.stdout.toString().split("\n").map((l) => l.trim()).filter((l) => /^[a-z][\w.-]*-[\w.-]+$/.test(l)).map((rule) => ({ rule, name: rule, fixKind: "unknown" }));
console.log(JSON.stringify(out));
