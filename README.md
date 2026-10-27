# fixhunt

**Finds linter autofixes that change what a program does. For the people who maintain the fixes.**

An autofix should be a refactoring: different code, same behaviour. fixhunt tests that claim by running code in a sandbox before and after the fix, not by asking a model.

- Each finding comes with a minimal reproducer, both outputs, the exact tool version, an advisory grade, an upstream search and an evidence sheet. Nothing is posted anywhere.
- Linters are JSON specs in `tools/*.json`; Biome, ruff, ESLint and clang-tidy ship.
- Nemotron models on Nebius Token Factory read, write and judge; Token Factory Sandboxes run the code.

## Judging

**Nebius x NVIDIA Global AI Hackathon, Coding and Agentic Engineering track.** 

Submission repository: [and2049/fixhunt](https://github.com/and2049/fixhunt).

Hosted dashboard: [fixhunt.onrender.com](https://fixhunt.onrender.com). Live hunts and scans need the access code from the Devpost submission; browsing findings does not.

Or run it locally with the Quick start below.

## Two ways to test a fix

**Hunt a rule.**
- Nemotron 3 Super reads the rule docs, lists the rewrite's semantic hazards and writes small deterministic programs around them.
- Each program is run twice, linted, fixed, syntax-checked, run again and re-linted in a fresh VM without network.
- Five model-free oracles: tool crash, fixed program does not parse, output or exit status changed, fix is not a fixpoint, failing fix labelled safe.
- Hits are minimized by delta debugging, confirmed, graded by Nemotron 3 Ultra, searched upstream (GitHub, Tavily) and written up.

**Scan a repository.**
- Each rule's fix is applied to a copy of a real project, one rule at a time, and the project's command runs before and after.
- A finding is a fix that changed the normalized output or exit status. It is reduced to a 1-minimal set of hunks, re-applied with git apply, re-linted, judged and searched upstream.
- Fixes with no difference are combined, run once more and published as a patch.
- By default: safe fixes among the rules the repository enables, known-risk rules first.

## Two findings in ruff

- **FURB103**, found by hunting the rule: `flag and f.write(x)` becomes an unconditional `Path(p).write_text(x)` ([astral-sh/ruff#29452](https://github.com/astral-sh/ruff/issues/29452)).
- **FURB129**, found by scanning a personal python project: `for line in fp` shares the file position with `fp.readline()` or `fp.seek()` in the loop body ([astral-sh/ruff#29640](https://github.com/astral-sh/ruff/issues/29640)).

Both were investigated and filed by hand.

Judge grades are advisory: 87% agreement with hand labels on 89 findings (`bun src/cli.ts judge-eval`).

## Quick start

```sh
bun install
cp .env.example .env            # NEBIUS_API_KEY, optional TAVILY_API_KEY
bun src/cli.ts hunt --tool ruff --rule FURB103 --n 8
bun src/cli.ts scan --tool ruff --dir demo/repo --run "cd python && python3 -m unittest discover -s tests -t ." --rules FURB103,FURB129,RUF019,PLR1733,UP015
bun src/cli.ts sweep --tool biome          # every Biome rule with a safe fix
bun src/cli.ts serve                       # dashboard at http://localhost:8731
bun test                                   # unit tests (hunk algebra, normalization, specs, fixtures)
```

- Requires [Bun](https://bun.sh), Node (Biome, ESLint), `uv` (ruff), Python 3, clang-tidy for the C++ spec.
- Code runs in [Token Factory Sandboxes](https://docs.tokenfactory.nebius.com/sandboxes/overview) when the key has access (`FIXHUNT_SANDBOX=auto`), otherwise under `bwrap`.
- A sandbox run is a fresh VM from `node:20-slim`, `python:3.12-slim` or `gcc:14`; about $0.001 and one to two seconds.
- `demo/repo` is a small Python, JavaScript and C++ project seeded with fixes that change behaviour next to harmless ones. Its README lists the shapes and scan commands.

## Dashboard

`serve` opens on the hunt and scan forms, with worked examples that prefill them (the scans target `demo/repo` in this repository), and streams every stage. A scan takes an optional subdirectory of the repository. Findings are grouped by rule and ranked, with filters in the URL hash.

- Finding page: the model's hazard and prediction, minimized program before and after, both outputs, grade, explanation, repro commands, upstream search, evidence sheet, a regression fixture to drop into the tool's test suite, re-run button.
- Scan page: smallest change per finding, output diff, sites left behind, judge, upstream, plus the no-difference patch.
- `render` exports the same pages as static HTML.
- Hosted: `Dockerfile` and `render.yaml` deploy it; `FIXHUNT_ACCESS` (see `.env.example`) gates live actions behind access codes.

## Where the models are used

| Stage | Model |
|---|---|
| Analyze, generate, dedup queries, explanation | `nvidia/nemotron-3-super-120b-a12b` |
| Judge, dedup triage | `nvidia/Nemotron-3-Ultra-550b-a55b` |
| Minimize proposal (oracle accepts or rejects) | `nvidia/Nemotron-3_5-Lightning` |

Calls use the OpenAI-compatible Token Factory endpoint. A 16-program hunt costs about a cent, a four-finding scan about two; spend is logged in `runs/spend.jsonl`.

## What a finding is not

- Not a proof for every input: it is one deterministic run. The judge is advisory.
- A scan observes one command; code it does not exercise is not observed.
- Hunts compare stdout, exit code and first stderr line; scans compare stdout and last stderr line after scrubbing timings, paths and positions.
- Fixers run on the host with repository config disabled (`ruff --isolated`, `eslint --no-config-lookup`, `clang-tidy --config={}`). Symbolic links are dropped from copies.
- Only GitHub issue and PR URLs count as upstream matches; "fixed in" notes are advisory.

## Tool specs

A tool is a JSON file describing version, rule lookup, lint, fix, syntax check, run, enabled rules and catalog. `src/tools/spec.ts` turns it into an adapter; copy `tools/ruff.json` and add yours to `tools/`, `FIXHUNT_TOOLS` or `--tool-file`.

## CLI

```
hunt      --tool <id> --rule <rule> [--n 8] [--rounds 1] [--unsafe] [--seed 1]
scan      --tool <id> --dir <checkout> --run "<command>" [--rules A,B] [--limit k] [--image img] [--no-net] [--timeout s]
          [--no-minimize] [--no-judge] [--no-upstream] [--no-combine] [--exclude a,b]
apply     scan, then git apply the no-difference fixes
risk      --tool <id> --dir <checkout>    enabled rules with a known finding
sweep     --tool <id> [--n 8] [--rounds 2] [--limit k] [--only regex] [--fresh]
check     --tool <id> --rule <rule> --file prog.<ext> [--report]
reprocess | refresh | triage | judge-eval | catalog | tools | serve | render
```

## Layout

```
src/cli.ts        commands
src/hunt.ts       hunt loop
src/oracles.ts    per-program pipeline and oracles
src/minimize.ts   ddmin
src/judge.ts      grading
src/dedup.ts      upstream search and triage
src/pipeline.ts   minimize, judge, dedup, report
src/report.ts     evidence sheets
src/scan.ts       repository scans
src/known.ts      config readers, findings bank
src/contree.ts    Token Factory Sandboxes client
src/sandbox.ts    sandbox, bwrap or plain exec
src/server.ts     dashboard server
src/web/          dashboard pages, static export
src/tools/        spec engine
tools/            tool specs
demo/repo         test repository
demo/findings     snapshot of runs/
data/             rule catalogs, judge labels
```

## License

MIT
