def gen():
    yield 1
    yield 2
g = gen()
x = next(g)
result = [z for z in g if x == z or x == z]
print('Result:', list(result))
