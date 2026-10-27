def f(*, default=[]):
    default.append(1)
    return default
x = f() if not False else f()
print(len(x))
