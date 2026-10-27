def gen():
    yield 1
    yield 2

g = gen()
print('First check:', next(g) is not None)
print('Second check:', next(g) is not None)
