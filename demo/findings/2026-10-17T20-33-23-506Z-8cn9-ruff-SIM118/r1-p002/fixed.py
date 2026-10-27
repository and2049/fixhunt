class Writer:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
with Writer() as w:
    d = {'x': 1}
    if 'x' in d:
        w.write('found')
print(''.join(w.data))
