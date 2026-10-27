def gen():
    yield 1
    yield 2

g = gen()
a = list(x for x in g)
b = list(x for x in g)
print('a:', a, 'b:', b)
