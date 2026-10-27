class Writable:
    def __enter__(self):
        self.data = []
        return self
    def write(self, x):
        self.data.append(x)
    def __exit__(self, *args):
        pass
with Writable() as w:
    w.write(str(bin(15).count('1')))
print(w.data)
