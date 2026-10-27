class Logger:
    def __init__(self):
        self.buf = []
    def write(self, data):
        self.buf.append(data)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass

log = Logger()
with log as l:
    msg = 'hello'
    msg = msg + ' world'
    l.write(msg)
print('log buf:', log.buf)
