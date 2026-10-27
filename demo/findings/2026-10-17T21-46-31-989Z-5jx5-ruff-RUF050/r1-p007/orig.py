def f(x=[]):
    if 0:
        pass
    x.append(1)
    return x
print(f())
print(f())
