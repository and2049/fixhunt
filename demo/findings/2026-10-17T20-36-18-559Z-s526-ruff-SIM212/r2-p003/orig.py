state = 0
def get():
    global state
    state += 1
    return state
a = get() if not False else 0
print(a, state)
