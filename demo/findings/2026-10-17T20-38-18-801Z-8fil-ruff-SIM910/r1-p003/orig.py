def make_getter(d):
    return lambda k: d.get(k, None)
d = {'a': 1}
getter = make_getter(d)
vals = [getter(k) for k in ['a', 'b']]
print(vals)
