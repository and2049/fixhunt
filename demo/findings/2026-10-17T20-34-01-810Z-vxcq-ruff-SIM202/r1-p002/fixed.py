def g(a, /, b, *, c=not 1 != 1, d):
    print(c, d)
g(1, 2, d=3)
