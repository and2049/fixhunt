log = []
class D:
    def __contains__(self, k):
        log.append(f'contains:{k}')
        return k == 'x'
    def __getitem__(self, k):
        log.append(f'getitem:{k}')
        return 1 if k == 'x' else None
    def get(self, k, default=None):
        log.append(f'get:{k}')
        return self[k] if k in self else default

def f(b):
    return b

d = D()
result = f("x" in d and d["x"])
print(f"original: {result}, log={log}")
log.clear()
result = f(d.get("x"))
print(f"after fix: {result}, log={log}")
