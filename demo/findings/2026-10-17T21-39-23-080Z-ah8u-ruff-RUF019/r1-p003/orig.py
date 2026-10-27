state = []
class D:
    def __contains__(self, k):
        state.append('contains')
        return k == 'x'
    def __getitem__(self, k):
        state.append('getitem')
        return 1 if k == 'x' else None
    def get(self, k, default=None):
        state.append('get')
        return self[k] if k in self else default

d = D()
if "x" in d and d["x"]:
    print("true", state)
else:
    print("false", state)
state.clear()
if d.get("x"):
    print("true after fix", state)
else:
    print("false after fix", state)
