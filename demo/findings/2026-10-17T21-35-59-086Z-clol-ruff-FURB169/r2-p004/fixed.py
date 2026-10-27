def gen():
    yield 1
    yield None

g = gen()
first = next(g)
if first is None:
    print('first is None')
else:
    print('first is not None:', first)
second = next(g)
if second is None:
    print('second is None')
else:
    print('second is not None:', second)
