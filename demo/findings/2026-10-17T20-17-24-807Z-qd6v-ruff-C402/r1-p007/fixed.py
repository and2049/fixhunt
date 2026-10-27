class Obj:
    def __init__(self, v):
        self.v = v
    def __bool__(self):
        return self.v % 2 == 0
    def __eq__(self, other):
        return isinstance(other, Obj) and self.v == other.v
data = [(Obj(1), Obj(2)), (Obj(3), Obj(4))]
d = dict((k, v) for k, v in data)
for k, v in d.items():
    print('key bool:', bool(k), 'value bool:', bool(v))
    print('k is Obj(1)?', k is Obj(1))
    print('k == Obj(1)?', k == Obj(1))
