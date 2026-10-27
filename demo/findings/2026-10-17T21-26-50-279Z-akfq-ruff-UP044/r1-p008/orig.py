from typing import Unpack
def f(x: Unpack[tuple[int, int]]):
    if x[0] == 0: raise ValueError('zero')
    return x[1] // x[0]
try:
    print(f(0, 5))
except ValueError as e:
    print('caught:', e)
else:
    print('no error')
finally:
    print('cleanup')
