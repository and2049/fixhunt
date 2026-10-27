call_log = []
class M:
    def __contains__(self, k): return k == 'x'
    def __getitem__(self, k):
        call_log.append(k)
        if k == 'x': return 0
        raise KeyError(k)
    def get(self, k, default=None):
        return self[k] if k in self else default

m = M()
if m.get("x"):
    print("block entered")
else:
    print("block skipped", call_log)
call_log.clear()
if m.get("x"):
    print("block entered after fix")
else:
    print("block skipped after fix", call_log)
