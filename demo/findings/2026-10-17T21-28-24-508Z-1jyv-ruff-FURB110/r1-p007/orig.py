class Writer:
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass
    def write(self, data):
        self.data = data

with Writer() as w:
    result = w.write('hi') if w.write('hi') else None
print('written:', getattr(w, 'data', None))
