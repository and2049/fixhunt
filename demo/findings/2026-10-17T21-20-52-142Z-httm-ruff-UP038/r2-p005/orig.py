def gen():
    yield 1
    yield 'a'
g = gen()
isinstance(next(g), (int, str))
try:
    isinstance(next(g), (int, str))
except StopIteration as e:
    print('StopIteration:', e)
