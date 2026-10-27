# Scan 2026-10-23T03-44-32-139Z-scan-clang-tidy

- Tool: clang-tidy 21.1.8
- Project: /home/sun/dev/diaghunt/demo/repo
- Command: `make -s -C native test`
- Rules tried: 3; fixes that changed files: 3; outcome changed: 2; no difference: 1
- Known-risk rules enabled here: none

## modernize-use-nullptr: fix-changes-behavior

Files changed: native/src/names.cpp, native/tests/tests.cpp. Exit 0 → 0. Smallest change: 1 of 2 hunk(s). Sites: 2 → 0.

Judge (advisory): introspection-only, low. The only difference is the test framework printing the rewritten source text 'nullptr' instead of 'NULL' in its diagnostic output. The rule replaces the NULL macro with nullptr, which is a source-text change that the test harness reflects in its 'ok' line. No runtime semantics, environment, or pre-existing failure is involved.

Upstream: related https://github.com/llvm/llvm-project/issues/23565

Evidence sheet: reports/modernize-use-nullptr.md

```
stdout lines only before the fix:
  ok   first_or_null("") == NULL
stdout lines only after the fix:
  ok   first_or_null("") == nullptr
```

```diff
--- a/native/tests/tests.cpp
+++ b/native/tests/tests.cpp
@@ -16,7 +16,7 @@
   Window off(0);
   CHECK(disabled(off));
   CHECK(normalize("MiXed") == "mixed");
-  CHECK(first_or_null("") == NULL);
+  CHECK(first_or_null("") == nullptr);
   CHECK(std::strcmp(first_or_null("a"), "a") == 0);
   std::cout << (failures ? "FAILED" : "PASSED") << "\n";
   return failures ? 1 : 0;
```

## readability-container-size-empty: fix-changes-behavior

Files changed: native/src/window.cpp. Exit 0 → 2. Smallest change: 1 of 1 hunk(s). Sites: 1 → 0.

Judge (advisory): real, high. The rule rewrites `w.size() == 0` to `w.empty()`, which for standard containers is semantically equivalent. However, the test failure indicates that `Window::empty()` either does not exist, has a different signature, or returns a different result than `w.size() == 0`. Since the documentation is missing and the fix is labelled unknown, the rewrite cannot be assumed safe for this user-defined type, and the change in test outcome demonstrates a real behavioral regression.

Upstream: related https://github.com/llvm/llvm-project/issues/171193, related https://github.com/llvm/llvm-project/issues/154762, related https://github.com/llvm/llvm-project/issues/152387, related https://github.com/llvm/llvm-project/issues/37603, related https://github.com/llvm/llvm-project/issues/118418, related https://github.com/llvm/llvm-project/issues/162287, related https://github.com/llvm/llvm-project/issues/185007, related https://github.com/llvm/llvm-project/issues/88203, related https://github.com/llvm/llvm-project/issues/72619, related https://github.com/llvm/llvm-project/issues/51118

Evidence sheet: reports/readability-container-size-empty.md

```
stdout lines only before the fix:
  ok   !disabled(w)
  PASSED
stdout lines only after the fix:
  FAIL !disabled(w)
  FAILED
exit 0 → 2
stderr last line before: (none)
stderr last line after: make: *** [Makefile:6: test] Error 1
```

```diff
--- a/native/src/window.cpp
+++ b/native/src/window.cpp
@@ -9,4 +9,4 @@
 
 int Window::sum() const { return std::accumulate(samples_.begin(), samples_.end(), 0); }
 
-bool disabled(const Window& w) { return w.size() == 0; }
+bool disabled(const Window& w) { return w.empty(); }
```

## Applied together

readability-redundant-string-cstr: 1 file(s); no difference under the command; accepted.patch applies with `git apply -p1`
