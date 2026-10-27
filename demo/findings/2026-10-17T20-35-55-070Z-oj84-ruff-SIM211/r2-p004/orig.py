from typing import List
T = False if True else True

def g(x: T) -> None:
    print('got', x)

g(1)
print('T=', T)
