def gen():
    yield 1
    yield 2

g = gen()
a = next(g)
b = list(g)
print(f'after first next: {a}, rest as list: {b}')

g2 = gen()
if not next(g2) == 1:
    print('unexpected')
else:
    print(f'remaining: {list(g2)}')
