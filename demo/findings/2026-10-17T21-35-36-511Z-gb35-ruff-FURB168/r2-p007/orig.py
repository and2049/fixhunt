counter = 0
def inc():
    global counter
    counter += 1
    return None
print(counter)
isinstance(inc(), type(None))
print('After:', counter)
counter = 0
print(counter)
result = inc() is None
print('After is None:', counter)
