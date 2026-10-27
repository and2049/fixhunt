def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(int(len(list(g))))
print(list(g))
