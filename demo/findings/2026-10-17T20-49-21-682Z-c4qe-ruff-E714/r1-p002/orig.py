from typing import List

def foo(x: List[int]) -> bool:
    return not x is None

print(foo([1]))
