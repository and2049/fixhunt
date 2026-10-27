import functools
lru = getattr(functools, 'lru_cache')
@lru(maxsize=None)
def f(x): return x + 1
print('Result:', f(5))
