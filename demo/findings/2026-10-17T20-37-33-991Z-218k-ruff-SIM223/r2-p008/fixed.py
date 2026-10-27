state = []
def log():
    state.append('log')
    return True
x = log()
res = x and [] and log()
print('state:', state)
print('res:', res)
