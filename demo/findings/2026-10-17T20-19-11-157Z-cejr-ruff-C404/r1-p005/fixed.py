counter = 0
def inc():
    global counter
    counter += 1
    return counter
d = dict([(inc(), inc()) for _ in range(2)])
print('counter:', counter, 'dict:', dict(d))
