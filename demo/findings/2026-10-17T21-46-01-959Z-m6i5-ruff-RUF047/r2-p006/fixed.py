def f(a, *, b=[]):
    if False:
        return
    b.append(a)
    return b
print(f(1))
print(f(2))
