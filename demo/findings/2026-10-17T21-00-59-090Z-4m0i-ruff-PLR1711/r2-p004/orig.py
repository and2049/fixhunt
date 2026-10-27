counter = 0

def inc():
    global counter
    counter += 1
    return counter

def f():
    a = inc()
    b = inc()
    return a + b

print(f())
