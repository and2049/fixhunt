def f():
    global \
        a
    global \
        b
    a = 1
    b = 2
    return a + b
print(f())
