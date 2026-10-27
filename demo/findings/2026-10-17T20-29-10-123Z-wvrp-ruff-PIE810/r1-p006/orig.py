class Writer:
    def __init__(self): self.buf = ''
    def write(self, data): self.buf += data
    def __enter__(self): return self
    def __exit__(self, *a): pass
s = 'msg'
if s.startswith('m') or s.startswith('mo'):
    with Writer() as w:
        w.write('ok')
    print(writer.buf if 'writer' in locals() else 'none')
