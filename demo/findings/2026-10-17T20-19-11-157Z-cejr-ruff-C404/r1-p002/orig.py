class LogWriter:
    def __enter__(self):
        self.buf = []
        print('enter')
        return self
    def __exit__(self, *exc):
        print('exit:', self.buf)
    def write(self, s):
        self.buf.append(s)
with LogWriter() as w:
    d = dict([(str(i), w.write(str(i))) for i in range(2)])
    w.write('done')
print('after')
