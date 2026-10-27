def f():
    i = [0]
    global a
    global b
    a = i[0]; i[0] += 1
    b = i[0]; i[0] += 1
    return a + b
print(f())
