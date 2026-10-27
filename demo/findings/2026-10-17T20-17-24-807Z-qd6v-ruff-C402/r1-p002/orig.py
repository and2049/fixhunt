state = []
def f():
    state.append(len(state))
    return len(state)
d = dict((f(), f()) for _ in range(2))
print('side effects:', state)
print('dict:', d)
