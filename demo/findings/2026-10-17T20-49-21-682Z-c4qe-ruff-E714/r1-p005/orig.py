def gen():
    yield 1
    yield 2

g = gen()
print('First check:', not next(g) is None)
print('Second check:', not next(g) is None)
