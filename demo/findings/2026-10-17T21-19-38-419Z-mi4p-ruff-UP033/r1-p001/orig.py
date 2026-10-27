import functools
N = [None]
decorator_factory = lambda _: functools.lru_cache(maxsize=N[0])
@decorator_factory(None)
def f(x): return x * 2
print('First:', f(5))
N[0] = 128
try:
    print('Second after rebind:', f(5))
except Exception as e:
    print(type(e).__name__, str(e))
