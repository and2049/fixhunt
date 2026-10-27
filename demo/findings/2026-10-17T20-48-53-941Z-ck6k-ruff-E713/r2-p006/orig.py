counter = 0
def inc():
    global counter
    counter += 1
    return counter
print(not inc() in [1, 2]))  # triggers; inc() called once
print('counter:', counter)
counter = 0
print(inc() not in [1, 2]))  # after fix equivalent
print('counter:', counter)
