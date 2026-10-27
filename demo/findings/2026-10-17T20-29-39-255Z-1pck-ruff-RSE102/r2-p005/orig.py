state = []
def side(x):
    state.append(x)
    return ValueError(x)
try:
    raise (side(1))()
except ValueError as e:
    print('Side effects:', state)
    print('Exception arg:', e.args[0])
state.clear()
try:
    raise side(2)()
except ValueError as e:
    print('Side effects after:', state)
    print('Exception arg:', e.args[0])
