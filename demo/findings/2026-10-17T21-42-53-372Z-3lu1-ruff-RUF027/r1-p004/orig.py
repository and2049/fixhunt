class LogSink:
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def write(self, msg): print('LOG:', msg.strip())
with LogSink() as sink:
    sink.write('Error: {code}'.format(code=500))
