def f(a, /, b, *, c=[]):
    global d, e
    return a + b + len(c) + d + e
d = 10
e = 20
print(f(1, 2, c=[3]))
