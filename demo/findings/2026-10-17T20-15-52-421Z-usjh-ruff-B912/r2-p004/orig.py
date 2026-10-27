class Obj:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return self.val is not None
    def __len__(self):
        return 0 if self.val is None else 1
objs = [Obj(1), Obj(None)]
vals = [1, None]
results = list(map(lambda o, v: (o is None) == (v is None), objs, vals))
print(results)
