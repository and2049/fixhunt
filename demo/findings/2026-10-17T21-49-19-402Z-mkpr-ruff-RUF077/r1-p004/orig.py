counter = 0

def get_default():
    global counter
    counter += 1
    return counter

def method(self=get_default()):
    return self

print(method())
print(method())
print(f'Counter: {counter}')
