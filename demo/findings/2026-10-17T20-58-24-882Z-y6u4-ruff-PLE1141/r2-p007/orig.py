# Simulate module side effect via function call
state = []

def init():
    state.append('loaded')
    return {'x': 1}

init()
print('State:', state)
for k, v in init():  # Trigger: function call returning dict
    print(k, v)
print('State after:', state)
