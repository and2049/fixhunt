class CM:
    def __enter__(self): return self
    def __exit__(self, *exc):
        if hasattr(self, 'seen') and 99 in self.seen:
            raise ValueError('99 seen')
with CM() as cm:
    s = {1, 2}
    cm.seen = set()
    for x in s:
        cm.seen.add(x)
        s.add(99)
print('ok')
