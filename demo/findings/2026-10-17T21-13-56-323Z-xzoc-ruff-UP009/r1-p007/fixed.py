class LogWriter:
    def __enter__(self):
        print('enter')
        return self
    def write(self, msg):
        print(f'log: {msg}')
    def __exit__(self, *exc):
        print('exit')
with LogWriter() as w:
    w.write('test')
