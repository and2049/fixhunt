state = []
def gen():
    state.append(1)
    return ['x','y']
d = dict.fromkeys(gen(), [])
print('state:', state)
print('d:', d)
