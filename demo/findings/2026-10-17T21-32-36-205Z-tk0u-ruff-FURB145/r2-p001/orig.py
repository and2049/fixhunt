state = []
def get_target(): return state[:]
state.append(1)
a = [] if False else get_target()
print('result id', id(a))
print('source len', len(state))
