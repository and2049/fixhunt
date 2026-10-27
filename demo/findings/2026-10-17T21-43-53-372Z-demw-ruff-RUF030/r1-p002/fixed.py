class Obj:
    def __init__(self, v): self.v = v
    def __str__(self): return f'<{self.v}>'
    def __repr__(self): return self.__str__()
out = []
for v in [1, 2]:
    o = Obj(v)
    try:
        assert v < 2, print(o)
    except AssertionError as e:
        out.append(str(e))
    else:
        out.append('no raise')
print('|'.join(out))
