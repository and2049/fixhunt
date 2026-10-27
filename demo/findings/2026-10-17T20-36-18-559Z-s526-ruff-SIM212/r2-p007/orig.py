def gen():
    yield 1
    yield 2
g = gen()
first = next(g) if not False else next(g)
print(first)
