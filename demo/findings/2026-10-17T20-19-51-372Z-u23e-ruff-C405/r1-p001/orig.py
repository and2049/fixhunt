def f(x=None):
    if x is None:
        x = []
    s = set(x)
    s.add(len(s))
    return s
print(f(), f())
