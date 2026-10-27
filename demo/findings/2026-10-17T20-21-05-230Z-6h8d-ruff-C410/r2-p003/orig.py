def g(*args, sep=':'):
    lst = list(args)
    return sep.join(map(str, lst))
print(g(1, 2, 3))
