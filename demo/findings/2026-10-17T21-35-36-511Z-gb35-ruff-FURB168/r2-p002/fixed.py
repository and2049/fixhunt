def gen():
    yield 1
g = gen()
next(g) is None  # First use consumes
try:
    next(g) is None
except StopIteration as e:
    print('StopIteration caught')
else:
    print('No exception')
