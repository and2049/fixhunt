def gen():
    yield 1
    yield 2
g = gen()
try:
    next(g)
    next(g)
    next(g)
except (StopIteration, Exception):
    print('caught:', type(e).__name__)
