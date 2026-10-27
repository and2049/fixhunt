def f():
    global a, b
    funcs = [(lambda: a + b) for _ in range(2) if (tmp := a) is not None]
    a = 10
    b = 20
    return [g() for g in funcs]
a = 0
b = 0
print(f())
