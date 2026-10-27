class Writer:
    def __enter__(self):
        self.data = []
        return self
    def __exit__(self, *exc):
        pass
    def write(self, s):
        self.data.append(s)
with Writer() as w:
    w.write('hello')
    idx = (0,)
    lst = ['world']
    lst[idx[0]] = w.data[0]
print('lst:', lst)
with Writer() as w:
    w.write('hello')
    idx = 0,
    lst = ['world']
    lst[idx[0]] = w.data[0]
print('lst:', lst)
