class A:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return isinstance(other, A) and self.v == other.v
    def __repr__(self): return f'A({self.v})'
a1, a2 = A(1), A(2)
s = set([a1, a2])
print(repr(s))
