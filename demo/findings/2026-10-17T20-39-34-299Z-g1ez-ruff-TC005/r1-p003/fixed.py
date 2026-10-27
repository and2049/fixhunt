def f(a=None):
    if a is None:
        a = []
    a.append(1)
    return a
print(f())
print(f())
