class W:
    def write(self, s): pass
    def __enter__(self): return self
    def __exit__(self, *a): pass
with W():
    pass
print('context manager used')
