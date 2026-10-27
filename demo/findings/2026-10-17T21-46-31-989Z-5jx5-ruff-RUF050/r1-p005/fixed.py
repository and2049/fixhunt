def g(a, /, b, *, c=print('default')):
    return a + b + len(str(c))
print(g(1, 2, c=3))
