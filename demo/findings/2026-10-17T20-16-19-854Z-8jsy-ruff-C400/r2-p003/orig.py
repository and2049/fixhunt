counter = 0

def get_foo():
    global counter
    counter += 1
    return [10, 20]

lst = list(x for x in get_foo())
print('counter:', counter, 'lst:', lst)
