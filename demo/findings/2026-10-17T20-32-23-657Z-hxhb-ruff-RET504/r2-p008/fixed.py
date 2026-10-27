def f():
    len = lambda x: 42
    x = len([1, 2, 3])
    return x
print(f())
print(len([1, 2, 3]))
