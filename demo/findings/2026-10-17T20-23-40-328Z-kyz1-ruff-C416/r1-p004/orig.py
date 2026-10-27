def g(d={k: k for k in range(2)}):
    d.append(99)
    return d
print('g():', g())
print('g():', g())
