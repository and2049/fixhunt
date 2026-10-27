def gen():
    yield 'a b'
g = gen()
for _ in g:
    pass
print('generator exhausted')
