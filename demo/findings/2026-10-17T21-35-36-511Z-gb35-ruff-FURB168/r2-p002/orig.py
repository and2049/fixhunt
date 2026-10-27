def gen():
    yield 1
g = gen()
isinstance(next(g), type(None))  # First use consumes
try:
    isinstance(next(g), type(None))
except StopIteration as e:
    print('StopIteration caught')
else:
    print('No exception')
