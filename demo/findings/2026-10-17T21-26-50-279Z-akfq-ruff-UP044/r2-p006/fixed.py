from typing import Unpack
side = []
def f():
    side.append(1)
    return (2,)
def g(*args: Unpack[tuple[int, ...]]):
    return side.pop() if side else 0
print(g(f()))
