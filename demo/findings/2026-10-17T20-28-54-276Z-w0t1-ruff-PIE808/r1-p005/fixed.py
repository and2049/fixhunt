def f(x=None, r=range(3)):
    if x is None:
        x = []
    x.extend(r)
    return x

print(f())
print(f())
