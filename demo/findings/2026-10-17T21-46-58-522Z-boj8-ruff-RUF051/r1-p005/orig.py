def bad_key():
    raise ValueError('bad key')
d = {'a': 1}
try:
    if bad_key() in d:
        del d[bad_key()]
except ValueError as e:
    print('Caught in condition:', type(e).__name__, str(e))
