def f(a, /, b, *, c=[]):  # noqa: INVALID
    c.append(1)
    return a, b, c
print(f(1, 2, c=3))
print(f(1, 2, c=4))
