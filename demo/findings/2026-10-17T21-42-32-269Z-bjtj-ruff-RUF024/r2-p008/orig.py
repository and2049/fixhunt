class Writer:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass  # no close

# Before fix: dict.fromkeys(['a'], Writer())  # all keys share same Writer instance
# After fix:  {k: Writer() for k in ['a']}  # each key gets new Writer
d = {k: Writer() for k in ['x', 'y']}
d['x'].write('hello')
print('d["y"].data:', d['y'].data)  # Should be [] if fix applied
