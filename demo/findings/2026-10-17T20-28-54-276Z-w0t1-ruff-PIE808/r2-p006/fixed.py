class K:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return self.v == other.v
    def __repr__(self): return f'K({self.v})'
d = {}
for i in range(2):
    d[K(i)] = i * 10
print('dict:', d)
print('keys:', list(d.keys()))
