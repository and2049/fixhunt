counter = 0

def get_x():
    global counter
    counter += 1
    return counter

def get_y():
    global counter
    counter += 10
    return counter

print((get_x() < get_y()) or not (get_x() < get_y()))
print('counter:', counter)
