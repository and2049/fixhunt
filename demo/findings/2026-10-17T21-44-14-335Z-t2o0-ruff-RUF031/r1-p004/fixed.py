class Writer:
    def __enter__(self):
        self.data = []
        return self
    def __exit__(self, *args):
        pass
    def write(self, v):
        self.data.append(v)
with Writer() as w:
    w.write([(1, 2)] [1, 2])
print(w.data[0][0])
