def f():
    global x
    global y
    def inner():
        return x + y
    x = 10
    y = 20
    return inner()
print(f())
print('x=', x, 'y=', y)
