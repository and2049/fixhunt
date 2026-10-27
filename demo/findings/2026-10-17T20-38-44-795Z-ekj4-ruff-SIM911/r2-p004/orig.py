def f(d={'a': 1, 'b': 2}):
    pairs = list(zip(d.keys(), d.values()))
    d['c'] = 3
    return pairs
print(f())
print(f({'x': 9}))
