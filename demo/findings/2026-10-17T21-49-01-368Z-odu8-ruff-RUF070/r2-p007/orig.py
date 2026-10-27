def gen():
    x = 42
    yield locals().get('x', 'missing')
print(list(gen()))
