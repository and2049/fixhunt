from typing import Unpack as U
def f(*args: U[tuple[int, ...]]) -> int:
    return sum(args)
print(f(1, 2, 3))
