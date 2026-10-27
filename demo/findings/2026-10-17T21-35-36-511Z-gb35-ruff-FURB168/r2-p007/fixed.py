counter = 0
def inc():
    global counter
    counter += 1
    return None
print(counter)
inc() is None
print('After:', counter)
counter = 0
print(counter)
result = inc() is None
print('After is None:', counter)
