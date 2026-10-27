from typing import Unpack
def gen(): yield 1; yield 2
values = gen()
def f(x: Unpack[tuple[int, int]]): return sum(x)
print(f(*values))
try:
    print(sum(values))
except TypeError as e:
    print('generator exhausted:', e)
