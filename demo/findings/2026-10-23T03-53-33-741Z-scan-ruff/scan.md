# Scan 2026-10-23T03-53-33-741Z-scan-ruff

- Tool: ruff ruff 0.17.1
- Project: /home/sun/dev/diaghunt/demo/repo
- Command: `cd python && python3 -m unittest discover -s tests -t .`
- Rules tried: 8; fixes that changed files: 8; outcome changed: 4; no difference: 4
- Known-risk rules enabled here: F632, RUF019, PLR1733, UP005, FURB129, PLR1736, C413, FURB103, FURB110, RUF051, SIM911, UP004, UP018, UP009, E714, RUF046, UP011

## FURB129: fix-changes-behavior

Files changed: python/toolbox/logs.py. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 1 → 0.

Judge (advisory): real, high. The fix replaces `fp.readlines()` with `fp`, changing the iteration from a pre-read list of lines to a live iterator over the file object. The program relies on `fp.seek(0)` inside the loop to restart reading from the beginning for each outer line, which works with `readlines()` because the outer iteration is over an in-memory list, but fails when iterating directly over `fp` because the file position is shared and the outer loop exhausts the iterator after the first inner pass.

Upstream: duplicate https://github.com/astral-sh/ruff/issues/29640, related https://github.com/astral-sh/ruff/issues/18843, related https://github.com/astral-sh/ruff/issues/17683, related https://github.com/astral-sh/ruff/issues/18231

Evidence sheet: reports/FURB129.md

```
exit 0 → 1
stderr last line before: OK
stderr last line after: FAILED (failures=1)
```

```diff
--- a/python/toolbox/logs.py
+++ b/python/toolbox/logs.py
@@ -4,7 +4,7 @@
 def has_duplicate(path):
     """True when any line occurs more than once. Each line is compared against a fresh pass over the file."""
     with open(path) as fp:
-        for line in fp.readlines():
+        for line in fp:
             fp.seek(0)
             if sum(1 for other in fp if other == line) > 1:
                 return True
```

## PLR1733: fix-changes-behavior

Files changed: python/toolbox/registry.py. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 1 → 0.

Judge (advisory): real, high. The fix incorrectly assumes the inner loop variable 'key' iterates over the outer dict's keys, but it actually iterates over 'value' (which could be a list or other iterable). Replacing 'table[key]' with 'value' substitutes the entire iterable for the specific looked-up element, changing the program's logic and causing a test failure.

Upstream: related https://github.com/astral-sh/ruff/issues/25182, related https://github.com/astral-sh/ruff/issues/29422, related https://github.com/astral-sh/ruff/issues/25150

Evidence sheet: reports/PLR1733.md

```
exit 0 → 1
stderr last line before: OK
stderr last line after: FAILED (failures=1)
```

```diff
--- a/python/toolbox/registry.py
+++ b/python/toolbox/registry.py
@@ -27,5 +27,5 @@
     out = {}
     for key, value in table.items():
         for key in value:
-            out[key] = table[key] if key in table else None
+            out[key] = value if key in table else None
     return out
```

## FURB103: fix-changes-behavior

Files changed: python/toolbox/config.py. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 2 → 0.

Judge (advisory): real, high. The fix replaces a conditional write (`enabled and f.write(text)`) with an unconditional `Path.write_text(text)`, changing the behavior when `enabled` is false: the original creates/truncates the file but writes nothing, while the fix always writes the text. The documentation presents the rewrite as equivalent for writing a single string, but does not account for guarded writes.

Upstream: duplicate https://github.com/astral-sh/ruff/issues/29452, related https://github.com/astral-sh/ruff/issues/26920, related https://github.com/astral-sh/ruff/issues/26922, related https://github.com/astral-sh/ruff/issues/20785

Evidence sheet: reports/FURB103.md

```
exit 0 → 1
stderr last line before: OK
stderr last line after: FAILED (failures=2)
```

```diff
--- a/python/toolbox/config.py
+++ b/python/toolbox/config.py
@@ -1,13 +1,12 @@
 """Write configuration files."""
+import pathlib
 
 
 def save(path, text, enabled):
     """Write `text` to `path` only when `enabled`; the file is created (and truncated) either way."""
-    with open(path, "w") as f:
-        enabled and f.write(text)
+    pathlib.Path(path).write_text(text)
 
 
 def save_count(path, text):
     """Write `text` and print the number of characters written."""
-    with open(path, "w") as f:
-        print(f.write(text))
+    pathlib.Path(path).write_text(text)
```

## RUF019: fix-changes-behavior

Files changed: python/toolbox/registry.py. Exit 0 → 1. Reduced to 1 of 1 hunk(s), confirmed. Sites in 1 file(s): 1 → 0.

Judge (advisory): real, high. The fix replaces `key in reg and reg[key]` with `reg.get(key)`, which changes behavior when the key exists but its value is falsy (e.g., 0, False, empty string). The original code returns None for falsy values, while the fixed code returns the falsy value itself, causing the function to return a falsy value instead of None and breaking the documented contract.

Upstream: related https://github.com/astral-sh/ruff/issues/14011, related https://github.com/astral-sh/ruff/issues/12953, related https://github.com/astral-sh/ruff/issues/12285

Evidence sheet: reports/RUF019.md

```
exit 0 → 1
stderr last line before: OK
stderr last line after: FAILED (errors=1)
```

```diff
--- a/python/toolbox/registry.py
+++ b/python/toolbox/registry.py
@@ -17,7 +17,7 @@
 
 def lookup(reg, key):
     """The registered value when present and truthy, else None."""
-    if key in reg and reg[key]:
+    if reg.get(key):
         return reg[key]
     return None
```

## Applied together

UP004, UP015, F541, I001: 1 file(s); no difference under the command; accepted.patch applies with `git apply -p1`
