def f():
    gen = (i for i in [1])
    x = list(gen)
    return x
print(f())
print(f())
