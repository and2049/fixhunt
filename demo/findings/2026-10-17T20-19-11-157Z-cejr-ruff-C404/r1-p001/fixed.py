def make_list():
    print('iterable')
    return [1, 2]
d = dict([(i, i*i) for i in make_list()])
print(dict(d))
