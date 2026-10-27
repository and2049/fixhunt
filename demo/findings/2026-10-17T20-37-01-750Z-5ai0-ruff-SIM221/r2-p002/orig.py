def gen():
    yield 1
    yield 2
g = gen()
a = next(g)
b = list(g) or not list(g)
print('first:', a, 'rest:', b)
