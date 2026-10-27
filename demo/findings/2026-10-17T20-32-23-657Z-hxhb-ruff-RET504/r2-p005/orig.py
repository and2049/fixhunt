def f():
    x = 10
    g = lambda: x
    x = 20
    return g()
print(f())
