class Writer:
    def __enter__(self): return self
    def __exit__(self, *exc): pass
    def write(self, s): self.data = s
with (Writer()) as w:
    w.write('test')
print(getattr(w, 'data', 'none'))
