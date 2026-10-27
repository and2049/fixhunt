open = lambda x: f'MOCK:{x}'
def load(p): return open(p)
print(load('/tmp/file'))
del open  # restore built-in
try:
    open('/tmp/file')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
