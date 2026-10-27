def f():
    global a
    global b
    s = f'{a} {b}'
    print(s)
a = 1
b = 2
f()
