counter = 0

def f():
    global counter
    counter += 1
    return 5

print(int(f()) + 1, counter)
