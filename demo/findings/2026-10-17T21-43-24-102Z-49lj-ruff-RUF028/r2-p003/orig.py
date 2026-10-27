# fmt: off
def f(a, /, b, *, c=[]):
    c.append(1)
    return a, b, c
print(f(1, 2))
print(f(1, 2))
