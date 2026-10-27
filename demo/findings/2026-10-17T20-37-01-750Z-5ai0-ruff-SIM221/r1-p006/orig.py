state = []

def log_and_return(val):
    state.append(val)
    return val

print(log_and_return(1) or not log_and_return(1))
print('state:', state)
