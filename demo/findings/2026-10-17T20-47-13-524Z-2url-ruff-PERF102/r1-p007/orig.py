def gen():
    yield ('a', 1)
    yield ('b', 2)
g = gen()
for k, _ in g:
    print(k, end='')
try:
    next(g)
    print('extra', end='')
except StopIteration:
    print('done', end='')
