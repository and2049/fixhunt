from typing import List
import sys
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    TypeAlias = type
MyList: TypeAlias = List[int]
def func() -> MyList:
    return [1, 2, 3]
x = func()
# No delattr here — this is a near-miss for the rule
print('x:', x)
print('type of x:', type(x))
