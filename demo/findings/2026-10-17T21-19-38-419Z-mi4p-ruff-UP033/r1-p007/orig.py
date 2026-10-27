import functools
kw = {'maxsize': None, 'typed': False}
@functools.lru_cache(**kw)
def h(x): return x * 3
print('Result with unpacked kwargs:', h(4))
