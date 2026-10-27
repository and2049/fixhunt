from typing import Unpack
def f(x: Unpack[tuple[int, ...]] = (), lst=[]):
    lst.extend(x)
    return lst
print(f(1, 2))
print(f(3))
print(f())
