import ast
import re
with open(__file__, 'r') as f:
    lines = f.readlines()
target_line = None
for i, line in enumerate(lines):
    if '# ruff: ignore[F401]' in line:
        target_line = i
        break
if target_line is None:
    print('suppression comment not found')
    exit(1)
comment = lines[target_line]
# Check if the comment has been rewritten to a name that is not the expected one for our intent
# We intended to suppress a hypothetical rule 'custom-rule', but we used F401.
# The fix will change it to 'unused-import'.
# If the fix produces a string that is not 'unused-import', we consider it incorrect for our intent.
# We look for the pattern ignore[...] and extract the content.
match = re.search(r'ignore\[([^]]+)\]', comment)
if not match:
    print('no ignore found')
    exit(1)
content = match.group(1)
# We expected the fix to produce 'unused-import' for F401
# If it produces something else, it's wrong for our goal (even if it's a valid rule)
if content == 'unused-import':
    print('suppression rewritten correctly for intent')
    print(42)
else:
    print(f'suppression rewritten to unexpected content: {content}')
    print(0)
