# toolbox (fixhunt demo repository)

A small multi-language project used to exercise fixhunt's repository scans: a Python package with
unittest tests, a JavaScript package with node:test tests, a C++ library with a Makefile, plus the
usual unrelated files (CI workflow, Dockerfile, data, scripts). Each language carries a few code shapes
on which a linter's automatic fix is known or suspected to change behaviour, next to ordinary code whose
fixes should be harmless.

| Tool | Command | Seeded shapes |
|---|---|---|
| ruff | `cd python && python3 -m unittest discover -s tests -t .` | FURB103 guarded write and printed write count (`toolbox/config.py`), FURB129 a `seek(0)` rescan inside a `readlines()` loop (`toolbox/logs.py`), RUF019 key check on a mapping without `.get` and PLR1733 shadowed loop key (`toolbox/registry.py`); UP015, UP004, F541, I001 on `toolbox/text.py` should apply cleanly |
| biome | `cd web && node --test` | useNumberNamespace with a parameter named `Number` (`src/parse.js`), noUselessElse hoisting a `let` into a collision (`src/branch.js`), noUselessLoneBlockStatements across a missing semicolon (`src/block.js`), noNegationElse on unbraced branches (`src/negate.js`); `src/util.js` should fix cleanly |
| eslint | `cd web && node --test` | `prefer-const`, `no-var`, `object-shorthand`, `prefer-template`, `no-else-return` on the same files; ESLint's `no-else-return` declines the `let` collision |
| clang-tidy | `make -s -C native test` | readability-container-size-empty on a type whose `size()` is not its element count (`include/window.hpp`); readability-redundant-string-cstr on `src/names.cpp` should apply cleanly; modernize-use-nullptr also rewrites `NULL` inside the test harness's stringified `CHECK(...)` text, which changes the printed output without changing behaviour (a case for the judge's introspection-only grade) |

Nothing here is a real product. Tests pass as committed; a behaviour change shows up as a failing test
or a changed test output.
