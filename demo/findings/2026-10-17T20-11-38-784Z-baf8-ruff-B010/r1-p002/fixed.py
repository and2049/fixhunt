state = []
def f():
    state.append(len(state))
    return [0, 0]
f().a = 99
print('state:', state)
