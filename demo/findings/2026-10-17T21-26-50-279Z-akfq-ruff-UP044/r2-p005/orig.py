from typing import Unpack
class A:
    def __bool__(self): return False
    def __len__(self): return 1
a = A()
def f(x: Unpack[tuple[A, ...]]) -> bool:
    return all(x)
print(f(a))
