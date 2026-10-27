def f(a, *, b=print('default') or 1):
    return a and not a
print(f(2))
print(f(2))
