state = 0

def inc():
    global state
    state += 1
    return state

r = range(0, inc())
print(list(r))
r = range(0, inc())
print(list(r))
