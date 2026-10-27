class K:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other):
        print(f'eq {self.v} == {other.v}')
        return self.v == other.v

vals = [K(1), K(2)]
d = {}
for k in vals:
    d[k] = False if k.v == 1 else True
print('dict:', [(k.v, v) for k, v in d.items()])
