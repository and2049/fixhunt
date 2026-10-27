class Writer:
    def __init__(self):
        self.buf = ''
    def write(self, s):
        self.buf += s
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass

with Writer() as w:
    data = {'msg': 'hello'}
    w.write(data.msg)
    w.write('\n')
print(w.buf)
