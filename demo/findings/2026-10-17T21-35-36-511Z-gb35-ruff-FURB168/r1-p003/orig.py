class Logger:
    def __enter__(self):
        self.buffer = []
        return self
    def __exit__(self, *exc):
        pass
    def write(self, s):
        self.buffer.append(s)
with Logger() as log:
    if isinstance(log, type(None)):
        log.write('is none')
    else:
        log.write('is logger')
print(''.join(log.buffer))
