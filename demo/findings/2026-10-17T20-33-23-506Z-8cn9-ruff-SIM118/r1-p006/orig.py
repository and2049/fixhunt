def f(/, a, *, b=None):
    d = {'k': 1}
    if b is None:
        b = []
    if 'k' in d.keys():
        b.append(d['k'])
    return b
print(f(1))
print(f(1))
