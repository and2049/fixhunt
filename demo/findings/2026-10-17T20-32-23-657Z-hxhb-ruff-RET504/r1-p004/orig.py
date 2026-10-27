def f(a=[]):
    x = a
    x.append(1)
    return x
print(f())
print(f())
