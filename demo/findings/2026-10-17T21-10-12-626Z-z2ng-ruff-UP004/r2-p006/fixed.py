counter = 0

def inc():
    global counter
    counter += 1
    return counter

class Test:
    x = inc()
    y = inc()

print(Test.x, Test.y, counter)
