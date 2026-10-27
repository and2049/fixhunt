def f():
    global x
    global y
    def inner():
        return x + y
    x = 1
    y = 2
    return inner()
x = 0
y = 0
print(f())
