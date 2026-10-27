class Log:
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def write(self, msg): print(f'LOG: {msg}')
with Log() as log:
    if hasattr(log, 'super'):
        log.super.write('test')  # triggers PLW0245 -> log.super().write('test')
    else:
        print('no super attr')
