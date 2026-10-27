def outer():
    x = []
    vals = [lambda i=i: x.append(i) for i in range(2)]
    f = vals[0] if not len(x) else vals[1]
    return f()
outer()
print(len(x))
