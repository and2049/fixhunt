# Scan 2026-10-23T03-53-12-014Z-scan-biome

- Tool: biome 2.5.15
- Project: /home/sun/dev/diaghunt/demo/repo
- Command: `cd web && node --test`
- Rules tried: 6; fixes that changed files: 5; outcome changed: 4; no difference: 1
- Known-risk rules enabled here: complexity/noUselessUndefinedInitialization, style/noUselessElse, complexity/noUselessLoneBlockStatements, complexity/noUselessThisAlias, complexity/useRegexLiterals, style/noNegationElse, style/useExponentiationOperator, style/useNumberNamespace, suspicious/noPrototypeBuiltins, complexity/noAdjacentSpacesInRegex, nursery/useVueBaseImport, complexity/useFlatMap

## style/noNegationElse: fix-breaks-build

Files changed: web/src/negate.js. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 1 → 0.

Judge (advisory): real, high. The fix rewrites `if (!ok) return a; else return b;` to `if (ok) return b else return a`, which is invalid JavaScript syntax because an `else` clause cannot directly follow a single-statement `if` without braces. The original code parses and runs correctly, but the fixed code throws a SyntaxError at parse time, breaking the build.

Upstream: related https://github.com/biomejs/biome/issues/11351, related https://github.com/biomejs/biome/issues/11558, related https://github.com/biomejs/biome/issues/8347, related https://github.com/biomejs/biome/issues/9629, related https://github.com/biomejs/biome/issues/7518, related https://github.com/biomejs/biome/issues/691

Evidence sheet: reports/style_noNegationElse.md

```
stdout lines only before the fix:
  # Subtest: pick
  ok 3 - pick
  # pass 5
  # fail 0
stdout lines only after the fix:
  # file:///w/web/src/negate.js:N
  #   if (ok) return b else return a
  #                    ^^^^
  # SyntaxError: Unexpected token 'else'
  #     at compileSourceTextModule (node:internal/modules/esm/utils:346:16)
  #     at ModuleLoader.moduleStrategy (node:internal/modules/esm/translators:146:18)
  #     at \#translate (node:internal/modules/esm/loader:497:12)
  #     at ModuleLoader.loadAndTranslate (node:internal/modules/esm/loader:544:27)
  # Node.js v20.20.0
  # Subtest: /w/web/test/negate.test.js
  not ok 3 - /w/web/test/negate.test.js
    location: '/w/web/test/negate.test.js:N'
    failureType: 'testCodeFailure'
    exitCode: 1
    signal: ~
    error: 'test failed'
    code: 'ERR_TEST_FAILURE'
  # pass 4
  # fail 1
exit 0 → 1
```

```diff
--- a/web/src/negate.js
+++ b/web/src/negate.js
@@ -1,4 +1,3 @@
 export function pick(ok, a, b) {
-  if (!ok) return a
-  else return b
+  if (ok) return b else return a
 }
```

## complexity/noUselessLoneBlockStatements: fix-changes-behavior

Files changed: web/src/block.js. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 1 → 0.

Judge (advisory): real, high. The rule removes a lone block that was intentionally placed to prevent the following line starting with '[' from being parsed as a computed member access on the preceding array literal. Without the block, '[0, 1].forEach(...)' becomes '[1, 2][0, 1].forEach(...)', which is a property access yielding undefined, causing a TypeError. The documentation claims such blocks are unnecessary, but in ASI-free code they serve as statement separators, so the rewrite is not semantics-preserving.

Upstream: duplicate https://github.com/biomejs/biome/issues/11935, related https://github.com/biomejs/biome/issues/834, related https://github.com/biomejs/biome/issues/8685, related https://github.com/biomejs/biome/issues/39

Evidence sheet: reports/complexity_noUselessLoneBlockStatements.md

```
stdout lines only before the fix:
  ok 1 - run logs both items
  # pass 5
  # fail 0
stdout lines only after the fix:
  not ok 1 - run logs both items
    location: '/w/web/test/block.test.js:N'
    failureType: 'testCodeFailure'
    error: '[1,2][(0 , 1)].forEach is not a function'
    code: 'ERR_TEST_FAILURE'
    name: 'TypeError'
    stack: |-
      run (file:///w/web/src/block.js:N)
      TestContext.<anonymous> (file:///w/web/test/block.test.js:N)
      Test.runInAsyncScope (node:async_hooks:206:9)
      Test.run (node:internal/test_runner/test:796:25)
      Test.processPendingSubtests (node:internal/test_runner/test:526:18)
      node:internal/test_runner/harness:255:12
      node:internal/process/task_queues:140:7
      AsyncResource.runInAsyncScope (node:async_hooks:206:9)
      AsyncResource.runMicrotask (node:internal/process/task_queues:137:8)
  # pass 4
  # fail 1
exit 0 → 1
```

```diff
--- a/web/src/block.js
+++ b/web/src/block.js
@@ -1,8 +1,6 @@
 // Written without semicolons; the lone block keeps the next line from being read as an index expression.
 export function run(log) {
   const items = [1, 2]
-  {
     [0, 1].forEach((i) => log(items[i]))
-  }
   return log
 }
```

## style/useNumberNamespace: fix-changes-behavior

Files changed: web/src/parse.js. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 1 → 0.

Judge (advisory): real, medium. The rule rewrites the global `parseInt` to `Number.parseInt`, but the function parameter is also named `Number`, shadowing the global `Number` namespace. After the fix, `Number.parseInt` resolves to the parameter (a function), which lacks a `parseInt` property, causing a TypeError. The documentation does not mention this shadowing scenario, so the fix is not safe for this construct.

Upstream: related https://github.com/biomejs/biome/issues/11351, related https://github.com/biomejs/biome/issues/11558, related https://github.com/biomejs/biome/issues/1228, related https://github.com/biomejs/biome/issues/3578, related https://github.com/biomejs/biome/issues/2075

Evidence sheet: reports/style_useNumberNamespace.md

```
stdout lines only before the fix:
  ok 4 - parseAll adds the converter's value
  # pass 5
  # fail 0
stdout lines only after the fix:
  not ok 4 - parseAll adds the converter's value
    location: '/w/web/test/parse.test.js:N'
    failureType: 'testCodeFailure'
    error: 'Number.parseInt is not a function'
    code: 'ERR_TEST_FAILURE'
    name: 'TypeError'
    stack: |-
      file:///w/web/src/parse.js:N
      Array.map (<anonymous>)
      parseAll (file:///w/web/src/parse.js:N)
      TestContext.<anonymous> (file:///w/web/test/parse.test.js:N)
      Test.runInAsyncScope (node:async_hooks:206:9)
      Test.run (node:internal/test_runner/test:796:25)
      Test.processPendingSubtests (node:internal/test_runner/test:526:18)
      node:internal/test_runner/harness:255:12
      node:internal/process/task_queues:140:7
      AsyncResource.runInAsyncScope (node:async_hooks:206:9)
  # pass 4
  # fail 1
exit 0 → 1
```

```diff
--- a/web/src/parse.js
+++ b/web/src/parse.js
@@ -1,4 +1,4 @@
 // Parse string values with a caller-supplied converter for the non-integer part.
 export function parseAll(values, Number) {
-  return values.map((v) => parseInt(v, 10) + Number(v));
+  return values.map((v) => Number.parseInt(v, 10) + Number(v));
 }
```

## style/noUselessElse: fix-breaks-build

Files changed: web/src/branch.js, web/src/negate.js, web/src/util.js. Exit 0 → 1. Reduced to 1 of 3 hunk(s), confirmed. Sites in 3 file(s): 3 → 0.

Judge (advisory): real, high. The fix hoists the `let text` declaration from the `else` block into the outer scope where `let text = "none"` already exists, creating a duplicate declaration that makes the file fail to parse. The documentation presents the rewrite as equivalent but does not account for variable shadowing across the removed block boundary.

Upstream: duplicate https://github.com/biomejs/biome/issues/11937, related https://github.com/biomejs/biome/issues/12529, related https://github.com/biomejs/biome/issues/11351, related https://github.com/biomejs/biome/issues/11558, related https://github.com/biomejs/biome/issues/11092, related https://github.com/biomejs/biome/issues/3770, related https://github.com/biomejs/biome/issues/1191, related https://github.com/biomejs/biome/issues/4354, related https://github.com/biomejs/biome/issues/8347; a snippet says fixed in 2.5.14 (https://github.com/biomejs/biome/issues/11937, advisory)

Evidence sheet: reports/style_noUselessElse.md

```
stdout lines only before the fix:
  # Subtest: label
  ok 2 - label
  # pass 5
  # fail 0
stdout lines only after the fix:
  # file:///w/web/src/branch.js:N
  #     let text = "non-positive";
  #         ^
  # SyntaxError: Identifier 'text' has already been declared
  #     at compileSourceTextModule (node:internal/modules/esm/utils:346:16)
  #     at ModuleLoader.moduleStrategy (node:internal/modules/esm/translators:146:18)
  #     at \#translate (node:internal/modules/esm/loader:497:12)
  #     at ModuleLoader.loadAndTranslate (node:internal/modules/esm/loader:544:27)
  # Node.js v20.20.0
  # Subtest: /w/web/test/branch.test.js
  not ok 2 - /w/web/test/branch.test.js
    location: '/w/web/test/branch.test.js:N'
    failureType: 'testCodeFailure'
    exitCode: 1
    signal: ~
    error: 'test failed'
    code: 'ERR_TEST_FAILURE'
  # pass 4
  # fail 1
exit 0 → 1
```

```diff
--- a/web/src/branch.js
+++ b/web/src/branch.js
@@ -2,8 +2,7 @@
   let text = "none";
   if (n > 0) {
     return "positive";
-  } else {
+  }
     let text = "non-positive";
     return text;
-  }
 }
```

## Applied together

style/useConst: 2 file(s); no difference under the command; accepted.patch applies with `git apply -p1`
