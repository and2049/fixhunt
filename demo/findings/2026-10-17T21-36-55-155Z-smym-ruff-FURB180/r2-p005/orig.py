class Logger(metaclass=abc.ABCMeta):
    def write(self, msg):
        self.buf += msg
    def __enter__(self):
        self.buf = ''
        return self
    def __exit__(self, *exc):
        print(f'Log: {self.buf}')
with Logger() as l:
    l.write('hello')
    l.write('world')
