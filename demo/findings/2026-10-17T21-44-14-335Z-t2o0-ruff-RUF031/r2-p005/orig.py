def gen():
    yield 1
    yield 2
g = gen()
d = {}
d[(next(g), next(g))] = 'got'
print('first access:', d[(1, 2)])
g = gen()
try:
    print('second access:', d[(next(g), next(g))])
except StopIteration as e:
    print('StopIteration:', e)
g = gen()
d = {}
d[(next(g), next(g))] = 'got'
print('first access:', d[(next(g), next(g))])
g = gen()
try:
    print('second access:', d[(next(g), next(g))])
except StopIteration as e:
    print('StopIteration:', e)
