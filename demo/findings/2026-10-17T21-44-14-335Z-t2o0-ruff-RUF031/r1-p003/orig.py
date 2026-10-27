def f():
    x = []
    if (x := [(1, 2)])[0]:
        pass
    return x
print(f())
