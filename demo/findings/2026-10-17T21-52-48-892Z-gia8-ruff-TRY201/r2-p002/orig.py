def gen():
    yield 1
    yield 2
g = gen()
try:
    next(g)
    raise RuntimeError('fail')
except RuntimeError as err:
    raise err
print(list(gen()))
