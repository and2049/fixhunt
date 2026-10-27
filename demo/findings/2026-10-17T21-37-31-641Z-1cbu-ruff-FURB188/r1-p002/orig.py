b = b'prefix'
p = b'pre'
try:
    if b.startswith(p):
        b = b[:-len(p)] if b.startswith(p) else b
    print(b)
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')
