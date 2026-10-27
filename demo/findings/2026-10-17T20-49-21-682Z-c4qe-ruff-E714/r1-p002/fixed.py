from typing import List

def foo(x: List[int]) -> bool:
    return x is not None

print(foo([1]))
