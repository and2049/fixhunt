from typing import Unpack
class Desc:
    def __get__(self, obj, owner): return 99
class C:
    x = Desc()
    def __init__(self, a: Unpack[tuple[int]]): self.y = self.x + a[0]
c = C((5,))
print(c.y)
