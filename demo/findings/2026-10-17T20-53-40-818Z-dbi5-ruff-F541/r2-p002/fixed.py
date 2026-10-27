class Logger:
    def __init__(self):
        self.buf = []
    def write(self, data):
        self.buf.append(data)
log = Logger()
with log:
    log.write('hello')
print(''.join(log.buf))
