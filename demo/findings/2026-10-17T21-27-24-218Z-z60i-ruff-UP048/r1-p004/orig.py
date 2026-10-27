class BadKey:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(int(self.v))
    def __eq__(self, other):
        return isinstance(other, BadKey) and self.v == other.v

m = {}
k = BadKey(1)
while 1:
    if k in m:
        break
    m[k] = 'found'
    k.v += 1
print(list(m.keys()))
