from __future__ import annotations

# Simulate a tool that checks for __future__ import presence via AST or module inspection
# We use a side effect: accessing __future__.annotations to simulate tool reliance
import sys
if 'annotations' in dir(__import__('__future__')):
    print('Tool sees: annotations feature available')
else:
    print('Tool sees: annotations feature NOT available')

# At runtime, annotations is always available in Python 3.7+, but tool may misbehave
# if it relies on the import line being present
print('Runtime: using annotations in type hint')
def f() -> int:  # This line may be misparsed by tool if import removed
    return 42
print(f())
