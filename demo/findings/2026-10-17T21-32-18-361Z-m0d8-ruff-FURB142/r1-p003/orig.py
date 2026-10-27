class Buffer:
    def __init__(self):
        self.buf = []
        self.flushed = False
    def write(self, data):
        self.buf.append(data)
    def flush(self):
        self.flushed = True
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass

log = Buffer()
with log as l:
    for n in [1, 2, 3]:
        l.write(f'num:{n}\n')

print(''.join(log.buf), 'flushed:', log.flushed)
