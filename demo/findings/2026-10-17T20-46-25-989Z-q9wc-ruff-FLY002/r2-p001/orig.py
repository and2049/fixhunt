def f():
    x = 1
    g = lambda: " ".join((y := x, x + 1))
    x = 2
    return g()
print(f())
