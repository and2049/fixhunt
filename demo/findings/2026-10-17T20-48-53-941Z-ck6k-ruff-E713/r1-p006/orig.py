from typing import List, Optional  # typing-only import
# Rule does NOT trigger on annotations
x: int = 5
y: List[int] = [1, 2, 3]
# This is not a containment test with 'not', so silent
if not hasattr(__import__('sys'), 'version'):
    pass
print('x:', x, 'y:', y)
