import sys
from typing import Unpack
if sys.version_info < (3, 11):
    print('skipping: Python <3.11')
else:
    def f(x: Unpack[tuple[int, int]]): return x[0] * 2
    print(f(3, 4))
