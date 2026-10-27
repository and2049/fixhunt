class Writable:
    def __enter__(self):
        self.data = []
        return self
    def write(self, x):
        self.data.append(x)
    def __exit__(self, *args):
        pass
with Writable() as w:
    w.write(str((15).bit_count()))
print(w.data)
