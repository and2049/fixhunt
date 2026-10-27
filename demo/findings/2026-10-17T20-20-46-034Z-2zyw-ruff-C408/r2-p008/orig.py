def gen():
    yield 1
    yield 2

g = gen()
print(list(g))
print(list(g))
