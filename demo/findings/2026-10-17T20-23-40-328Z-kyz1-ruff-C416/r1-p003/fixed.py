state = []
def make_items():
    state.append(1)
    return [('x', 99)]
def f(d={k: v for k, v in make_items()}):
    return len(d)
print('state after def:', state)
print('f():', f())
print('state after call:', state)
