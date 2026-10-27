counter = 0
def get_type():
    global counter
    counter += 1
    return int if counter == 1 else str
x = 5
print(isinstance(x, get_type()) or isinstance(x, get_type()))
print('counter:', counter)
