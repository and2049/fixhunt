state = 0

def get_exc():
    global state
    state += 1
    return ValueError

try:
    raise get_exc()
except get_exc() as e:
    print('state:', state, 'exc:', type(e).__name__)
