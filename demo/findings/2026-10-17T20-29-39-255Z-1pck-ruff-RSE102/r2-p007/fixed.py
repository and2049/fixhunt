class Logger:
    def __init__(self): self.buf = []
    def write(self, s): self.buf.append(s)
    def __enter__(self): return self
    def __exit__(self, *exc): pass

log = Logger()
with log as l:
    try:
        l.write('before')
        raise (RuntimeError('bad'))()
    except RuntimeError:
        l.write('after')
print('Logged:', ''.join(log.buf))
