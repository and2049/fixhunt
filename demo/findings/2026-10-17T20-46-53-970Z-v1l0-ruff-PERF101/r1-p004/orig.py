def gen():
    yield 1
    raise ValueError('bad')
g = gen()
try:
    for x in list(g):
        print(x)
    print('else')
except ValueError as e:
    print('caught:', e)
else:
    print('no except')
finally:
    print('finally')
