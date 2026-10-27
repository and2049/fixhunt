class Writer:
    def __enter__(self):
        self.data = []
        return self
    def __exit__(self, *exc):
        pass
    def write(self, s):
        self.data.append(s)
with Writer() as w1, Writer() as w2:
    if 1 < 2 and 2 < 3:
        w1.write('hello')
        w2.write('world')
print(''.join(w1.data), ''.join(w2.data))
