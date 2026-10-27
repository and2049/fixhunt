Reviewed the requested docs and every file under `src/` and `tools/`. No files changed. Read-only probes confirmed directory escape, malformed-JSON acceptance, template corruption, and invalid rerun JavaScript; other findings follow from code inspection. No paid hunts or untrusted programs were executed.

Findings are ranked by severity.

1. **Critical — Generated programs can execute without isolation or read host secrets.** `src/sandbox.ts:37,62–70`; `src/minimize.ts:36`. Missing bubblewrap silently falls back to a normal process; working bubblewrap exposes the entire host filesystem read-only and inherits credentials through `process.env`.  
   **Scenario:** generated Python reads `.env` or SSH keys and prints them into findings; without bubblewrap it can modify host files or access the network. Minimization forces this local path even when remote sandboxes work.  
   **Fix:** fail closed; mount only required runtime files, clear the environment, and explicitly configure permitted writable directories.

2. **High — Unauthenticated server endpoints permit execution and spending abuse.** `src/server.ts:65–103`. The server specifies no loopback hostname, authentication, origin validation, or rerun concurrency limit.  
   **Scenario:** a reachable client repeatedly POSTs reruns, spawning unlimited concurrent evaluations and retaining temporary directories; a cross-origin request can trigger reruns without reading responses. Hunts also have no cumulative spending budget.  
   **Fix:** default to loopback, require authentication and origin checks, enforce a shared job queue and budget, and remove temporary directories in `finally`.

3. **High — Rule IDs can escape the run directory.** `src/server.ts:30`; `src/hunt.ts:29`; `src/check.ts:11`. Validation permits slashes and `..`, while directory construction replaces only the first slash.  
   **Scenario:** `misc-x/a/../../../../tmp/fixhunt-review` passes server validation; the hunt path construction resolves outside `runs/`. The clang-tidy adapter does not validate the rule against a catalog.  
   **Fix:** use an opaque run ID, store the rule separately, and verify resolved paths remain beneath their intended root.

4. **High — Local parsing and compilation remain outside the security boundary.** `src/tools/spec.ts:186–221`; `tools/clang-tidy.json:29`. Checks, linters, fixers, and compilation consume untrusted source with host access.  
   **Scenario:** generated C++ includes an absolute host file; compiler diagnostics can disclose its contents. Compilation bombs can exhaust host memory before program execution reaches a sandbox.  
   **Fix:** isolate the entire source-processing pipeline, including compiler and linter invocations, with restricted mounts and resource limits.

5. **High — Output limits do not prevent memory exhaustion.** `src/sandbox.ts:70–110`; `src/contree.ts:40–46`. Local output is accumulated without a bound and truncated only afterward; tarballs are also buffered completely.  
   **Scenario:** a program prints gigabytes within five seconds, exhausting the server before timeout. Without PID isolation, killing only the direct child can leave descendants and stream collectors alive.  
   **Fix:** bound collection while streaming, terminate on overflow, cancel readers, kill process groups, impose memory/PID limits, and cap archive sizes.

6. **High — Infrastructure failures become semantic findings.** `src/sandbox.ts:57–58`; `src/oracles.ts:119–127`; `src/scan.ts:66–69`. Remote execution failures are represented as ordinary results, but only the initial baseline receives special handling.  
   **Scenario:** the original runs successfully, then sandbox spawning fails for the fixed program; the oracle reports changed behavior. A timed-out syntax checker similarly becomes “fix breaks syntax.”  
   **Fix:** represent infrastructure errors separately; retry or mark evaluations inconclusive before comparing behavior.

7. **High — Failed confirmation does not prevent publication.** `src/pipeline.ts:40–54`. Failed remote confirmation retains local evidence, and an old minimized report can cause confirmation to be skipped after a new minimization.  
   **Scenario:** a candidate reproduces only under local Clang or host state, fails under the advertised sandbox environment, yet receives a normal evidence sheet. The fallback can even reuse the original finding when the current result lacks it.  
   **Fix:** require successful confirmation of the exact reported source; preserve failed confirmations as explicitly unverified candidates.

8. **High — Local executions share mutable state across comparisons.** `src/oracles.ts:64–87,125`; `src/scan.ts:39–66`. Bubblewrap mounts the working directory writable, and subsequent executions reuse it.  
   **Scenario:** a program prints the same output twice while creating a marker that changes its third execution; the changed output is attributed to the fix. Scan baselines can leave build artifacts that contaminate every rule copy.  
   **Fix:** run every baseline and fixed execution from independent copies of one immutable input snapshot.

9. **High — Refresh can delete valid findings after transient failures.** `src/reprocess.ts:44–55`. Every missing finding is treated as evidence that the defect disappeared.  
   **Scenario:** a sandbox outage or temporary nondeterminism sets `r.error`; refresh removes the report and its original finding.  
   **Fix:** distinguish failed evaluations from completed negative reproductions; retain history and require successful repeated checks before retiring findings.

10. **High — Scan uploads secrets and enables network access by default.** `src/scan.ts:15,28–40`; `src/contree.ts:53–61`. Repository copies exclude caches but include `.env`, credentials, and unrelated private files.  
    **Scenario:** scanning a normal application uploads its production credentials; repository test/install code can transmit them because networking defaults on.  
    **Fix:** exclude sensitive files by default, provide an explicit upload manifest, isolate dependency installation, and default test execution to no network.

11. **High — Model-generated duplicate URLs become executable links.** `src/dedup.ts:93`; `src/web/pages.ts:94,180`. Verdict URLs are not checked against retrieved hits or restricted to HTTPS; HTML escaping does not neutralize `javascript:` URLs.  
    **Scenario:** a hallucinated or prompt-injected verdict produces a link that executes script when clicked.  
    **Fix:** accept verdicts only for canonical URLs already present in validated search results; enforce scheme, hostname, repository, and issue-path checks.

12. **Medium — Static file serving follows symlinks outside its roots.** `src/server.ts:58–62`. Lexical checks do not establish filesystem containment.  
    **Scenario:** `examples/leak.py` or a report file symlinks to a readable host secret, which the server returns. This requires a symlink to exist; it is not an unrestricted URL-only traversal.  
    **Fix:** verify canonical paths beneath explicit roots and reject symlinks/nonregular files, preferably using race-resistant file opening.

13. **Medium — Fixed programs are executed only once.** `src/oracles.ts:83–88,125`. Only the original receives a determinism check, despite the documentation promising twice for both versions.  
    **Scenario:** a fix exposes randomized iteration; a single matching sample misses the change, while an anomalous sample is presented as stable evidence.  
    **Fix:** repeat both versions under identical conditions and classify unstable outcomes separately.

14. **Medium — Fixpoint detection does not test a fixpoint.** `src/oracles.ts:117,133–134`. Diagnostic counts neither establish idempotence nor identify newly introduced diagnostics.  
    **Scenario:** two diagnostics become one that a second fix would remove: missed finding. Conversely, fixing one issue while leaving a nonfixable issue can preserve the count and produce a false positive. `fix-introduces-diagnostic` is never emitted.  
    **Fix:** apply the fixer a second time and compare source; separately compare diagnostic identities and fixability.

15. **Medium — Output normalization loses real changes and retains irrelevant noise.** `src/oracles.ts:33–54`; `src/scan.ts:17–22`; `src/sandbox.ts:109`. Hunt compares only one stderr line and truncated stdout; scan ignores stderr and globally scrubs numeric-looking content.  
    **Scenario:** different equal-length stdout tails compare equal; stderr-only scan regressions disappear; printed `10s` and `20s` become identical. Remote `/w` paths are not normalized using the host working-directory path.  
    **Fix:** compare full-stream hashes plus bounded displays, retain meaningful stderr, and use narrow runner-specific normalization with raw evidence preserved.

16. **Medium — Diagnostic parsing accepts invalid schemas and inconsistent rule selection.** `src/tools/spec.ts:151–183`. A valid JSON object with missing/nonarray `items` becomes a clean lint result; JSON diagnostics are not filtered to the requested rule, unlike regex diagnostics.  
    **Scenario:** a tool changes its output shape to `{"error":"..."}` and every program appears silent; unrelated diagnostics can mark the target as fired or safe.  
    **Fix:** validate output schemas, explicitly select the target rule, and distinguish parse failures from tool crashes.

17. **Medium — Template substitution corrupts literal code and lacks a shell-safe contract.** `src/tools/spec.ts:76–90,195–196`; `tools/clang-tidy.json:33`. Unknown `{name}` sequences disappear, split variables ignore quoting, and unsafe arguments are inserted before the last argument regardless of file position.  
    **Scenario:** `echo ${HOME} {literal}` renders as `echo $ `; paths containing spaces break shell commands; custom shell templates interpolate rule IDs as executable syntax.  
    **Fix:** define escaped literal braces, reject unknown placeholders, support structured argv variables and explicit unsafe placeholders, and pass dynamic shell values as positional arguments.

18. **Medium — Sandbox polling can retry forever.** `src/contree.ts:71–85`. HTTP 429/5xx responses `continue` before checking the deadline.  
    **Scenario:** persistent service failure holds the server’s only hunt slot indefinitely. Advertised concurrency limits are fetched but unused.  
    **Fix:** check an overall deadline on every iteration, bound retries, add cancellation, and enforce provider limits through a shared semaphore.

19. **Medium — Sandbox selection is process-global and races between jobs.** `src/sandbox.ts:28–39`. `localOnly` affects every concurrent execution, not just minimization.  
    **Scenario:** a dashboard rerun launched during minimization unexpectedly runs locally; overlapping operations can also undermine remote confirmation.  
    **Fix:** pass execution policy explicitly or scope it with async-local context.

20. **Medium — Runs lack durable checkpoints and atomic replacement.** `src/hunt.ts:64,83–88`; `src/pipeline.ts:64–70`; `src/reprocess.ts:28`. Results are written only after all processing, directly to the final JSON path.  
    **Scenario:** a late search timeout loses the discoverable record of an expensive completed hunt; interruption during rewriting corrupts an existing run. Worker rejection does not cancel remaining workers.  
    **Fix:** checkpoint evaluations and reports incrementally, atomically rename completed JSON, serialize writers, and preserve failed/incomplete job states.

21. **Medium — Resume and caches ignore version and configuration.** `src/sweep.ts:16–33`; `src/catalog.ts:10–15`; `src/reprocess.ts:25`. Resume skips failed rules, caches key only on tool ID, and reprocessing executes current binaries while retaining the historical version.  
    **Scenario:** upgrading a linter skips its entire prior sweep; refreshed evidence is labelled with a version that never produced it.  
    **Fix:** fingerprint tool version/spec/options, retry failures, and record fresh execution provenance.

22. **Medium — Scan assumes every file fixer supports repository-wide fixing.** `src/scan.ts:60–63,83–85`. Passing `"."` through a single-file API fails for tools such as clang-tidy, and fixer/diff errors become skipped or “no change” outcomes.  
    **Scenario:** an unsupported repository scan finishes with zero findings; scanning fixhunt itself with output beneath the source fails the copy operation.  
    **Fix:** declare repository capabilities, enumerate supported files or use a dedicated repository command, report incomplete coverage, and place workspaces outside the source tree.

23. **Medium — Production judging differs from judge evaluation.** `src/pipeline.ts:58`; `src/judgeeval.ts:16–19,31`. Production omits before/after snapshots, disabling the pre-existing-failure hint used in evaluation; labels are assigned per rule rather than per finding.  
    **Scenario:** unrelated reproducers for one rule inherit one ground-truth label, while production lacks information credited for calibration improvements.  
    **Fix:** use one shared judge-input builder and label immutable individual findings.

24. **Medium — Run pages and the rerun button are broken.** `src/server.ts:77–82`; `src/web/pages.ts:82`. The `/r/` match is overwritten before use, and the server template emits a literal newline inside a JavaScript string.  
    **Scenario:** run links return 404; finding-page JavaScript fails to parse, so rerun never starts. Both failures are deterministic.  
    **Fix:** handle each route immediately and move client code to a separate script or correctly escape the newline.

25. **Medium — CLI flags and custom-tool registration are inconsistent.** `src/cli.ts:13–18`; `src/server.ts:16`. Boolean flags consume the next argument, and the server loads its registry before CLI extra specs are applied.  
    **Scenario:** `--unsafe --n 8` silently leaves unsafe mode disabled; `serve --tool-file custom.json` omits the custom tool.  
    **Fix:** use a typed argument parser and inject the finalized registry into the server.

Things done well:

- Ordinary tool commands use argv arrays, limiting shell-injection exposure.
- Sandbox command arguments are shell-quoted; archive bytes travel through stdin.
- Original programs receive syntax, termination, and repeated-execution checks.
- Minimization preserves the baseline exit/error shape, reducing meaningless reductions.
- Reports preserve source, diffs, evidence, and advisory judgments without automatically posting upstream.
