import functools
none_val = None
@functools.lru_cache(maxsize=none_val)
def f(x): return x + 10
print('Result with var maxsize:', f(5))
