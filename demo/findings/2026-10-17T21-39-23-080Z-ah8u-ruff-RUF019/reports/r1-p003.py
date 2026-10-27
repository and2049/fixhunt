state = []
class D:
    def __contains__(self, k):
        return k == 'x'
    def __getitem__(self, k):
        return 1 if k == 'x' else None
d = D()
if "x" in d and d["x"]:
    print("true", state)
