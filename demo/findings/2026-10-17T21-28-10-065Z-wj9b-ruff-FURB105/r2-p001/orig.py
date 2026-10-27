class K:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return isinstance(other, K) and self.v == other.v
k1 = K(1)
k2 = K(2)
d = {}
d[k1] = 'first'
d[''] = 'empty'
d[k2] = 'second'
print(len(d))
for k, v in d.items():
    print(f'{k.v if isinstance(k, K) else repr(k)}:{v}', end=' ') if hasattr(k, 'v') else None
