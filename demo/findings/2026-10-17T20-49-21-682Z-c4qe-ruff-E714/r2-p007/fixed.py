class A:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return self.v == other.v
a = A(1)
b = A(1)
d = {a: 'x'}
if d.get(b) is not None:
    print('found:', d[b])
else:
    print('missing')
