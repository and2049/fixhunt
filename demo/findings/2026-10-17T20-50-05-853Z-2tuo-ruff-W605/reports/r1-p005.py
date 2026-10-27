class Logger:
    def __init__(self):
        self.buf = []
    def write(self, msg):
        self.buf.append(msg)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
with Logger() as log:
    log.write('\_')
