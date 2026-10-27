state = []
def f():
    state.append(len(state))
    return [0, 0]
setattr(f(), 'a', 99)
print('state:', state)
