class Logger:
    def write(self, msg): print('LOG:', msg)
    def __enter__(self): return self
    def __exit__(self, *exc): pass
cache = {}
obj = Logger()
with cache.get('logger', None) or Logger() as log:
    log.write('test')
print('done')
