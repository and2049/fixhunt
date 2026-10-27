def f(d={'x': 1}):
    if 'x' in d:
        del d['x']
    return d
print('First call:', f())
print('Second call:', f())
