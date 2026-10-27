open = lambda x: f'MOCK:{x}'
def load(p): return open(p)
print(load(u'/tmp/file'))
del open  # restore built-in
try:
    open(u'/tmp/file')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
