counter = 0

def side_effect():
    global counter
    counter += 1
    return 5

print(int(side_effect() + 3), counter)
