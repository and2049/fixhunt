class LogStream:
    def __init__(self): self.buf = []
    def write(self, s): self.buf.append(s)
    def __enter__(self): return self
    def __exit__(self, *_:): pass
with LogStream() as ls:
    ls.write('x')
    s = set([ls])
    print(id(s), len(s))
