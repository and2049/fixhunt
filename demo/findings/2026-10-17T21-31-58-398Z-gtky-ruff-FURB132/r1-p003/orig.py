def f(x, s={1, 2, 3}):
    if x in s:
        s.remove(x)
    return s
print('First call:', f(2))
print('Second call:', f(1))  # s is mutated across calls
