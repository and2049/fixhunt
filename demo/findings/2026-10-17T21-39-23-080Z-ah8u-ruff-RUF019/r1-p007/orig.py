class D:
    def __contains__(self, k): return k == 'x'
    def __getitem__(self, k):
        if k == 'x': raise ValueError('bad')
        return None
    def get(self, k, default=None):
        try:
            return self[k]
        except ValueError:
            return default

d = D()
try:
    if "x" in d and d["x"]:
        print("yes")
except ValueError as e:
    print(f"caught: {e}")
else:
    print("no exception")
try:
    if d.get("x"):
        print("yes after get")
except ValueError as e:
    print(f"caught after get: {e}")
else:
    print("no exception after get")
