counter = 0
def get_obj():
    global counter
    counter += 1
    return type('O', (), {'attr': counter})()
del get_obj().attr  # triggers rule
print('counter:', counter)
