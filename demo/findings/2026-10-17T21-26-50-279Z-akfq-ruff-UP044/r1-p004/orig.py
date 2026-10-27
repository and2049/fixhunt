from typing import Unpack
side = 0
def get_values():
    global side
    side += 1
    return (side, side*2)
def f(x: Unpack[tuple[int, int]]): return x[0] + x[1]
print(f(*get_values()))
print('side effect count:', side)
