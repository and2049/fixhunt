state = 0
def side_effect():
    global state
    state += 1
    return state
class Exc(Exception):
    def __init__(self):
        self.val = side_effect()
try:
    raise Exc()
except Exception as e:
    print(f'First: {e.val}, Second: {side_effect()}')
    raise e  # Uses e.val after first side_effect()
