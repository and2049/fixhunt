class WriteOnly:
    def __enter__(self):
        self.data = []
        return self
    def write(self, x):
        self.data.append(x)
    def __exit__(self, *args):
        pass

with WriteOnly() as w:
    w.write('hello')
    w.write('world')
print('Written:', ''.join(w.data))
