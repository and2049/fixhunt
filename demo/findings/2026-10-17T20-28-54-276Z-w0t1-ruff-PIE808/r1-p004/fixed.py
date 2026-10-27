state = 0

def inc():
    global state
    state += 1
    return state

r = range(inc())
print(list(r))
r = range(inc())
print(list(r))
