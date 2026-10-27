class Log:
    def __enter__(self):
        self.log = []
        return self
    def write(self, msg):
        self.log.append(msg)
    def __exit__(self, *exc):
        pass  # removal doesn't affect __exit__ signature
with Log() as l:
    l.write('test')
    raise ValueError('oops')
print('logged:', l.log)
