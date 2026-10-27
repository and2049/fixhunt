state = []
def log(x):
    state.append(x)
    return x
def f():
    a = log(1)
    b = log(2)
    pass  # removal shouldn't change order
    return a + b
print(f(), state)
