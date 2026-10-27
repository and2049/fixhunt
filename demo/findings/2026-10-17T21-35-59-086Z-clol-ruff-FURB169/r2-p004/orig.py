def gen():
    yield 1
    yield None

g = gen()
first = next(g)
if type(first) is type(None):
    print('first is None')
else:
    print('first is not None:', first)
second = next(g)
if type(second) is type(None):
    print('second is None')
else:
    print('second is not None:', second)
