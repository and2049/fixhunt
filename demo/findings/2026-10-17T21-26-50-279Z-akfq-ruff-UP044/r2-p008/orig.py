from typing import Unpack
class B:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return self.v == other.v
b1, b2 = B(1), B(2)
def f(**kw: Unpack[dict[str, B]]) -> None:
    print(list(kw.keys()))
f(b1=b1, b2=b2)
