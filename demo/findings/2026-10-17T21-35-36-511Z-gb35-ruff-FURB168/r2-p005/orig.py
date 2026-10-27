class SilentWriter:
    def write(self, msg):
        pass
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass
with SilentWriter() as w:
    w.write('test')
    result = isinstance(w, type(None))
    print('isinstance result:', result)
