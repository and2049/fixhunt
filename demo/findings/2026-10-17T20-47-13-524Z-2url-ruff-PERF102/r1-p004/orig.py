def g(d={}):
    for k, _ in d.items():
        d[k] = 0
    return d
print(g({1: 2}))
print(g({}))
