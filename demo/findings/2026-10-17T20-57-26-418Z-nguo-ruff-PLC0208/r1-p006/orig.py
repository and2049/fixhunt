class Obj:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return isinstance(other, Obj) and self.v == other.v
    def __repr__(self): return f'Obj({self.v})'
s = {Obj(1), Obj(2)}
print([obj.v for obj in s])
