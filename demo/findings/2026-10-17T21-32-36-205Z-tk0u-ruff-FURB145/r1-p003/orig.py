def f(x=None):
    if x is None:
        x = []
    y = x[:]
    y.append(99)
    return x, y
a, b = f()
print('first call:', a, b)
c, d = f()
print('second call:', c, d)
