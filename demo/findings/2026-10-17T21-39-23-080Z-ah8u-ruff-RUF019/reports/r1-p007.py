class D:
    def __contains__(self, k): return k == 'x'
    def __getitem__(self, k):
        if k == 'x': raise ValueError('bad')
        try:
            return self[k]
        except ValueError:
            return default
d = D()
try:
    if "x" in d and d["x"]:
        print("yes after get")
except ValueError as e:
    print("no exception after get")
