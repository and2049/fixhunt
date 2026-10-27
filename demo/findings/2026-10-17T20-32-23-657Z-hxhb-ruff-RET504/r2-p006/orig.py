def f():
    x = (yield 1)
    return x
print(list(f()))
