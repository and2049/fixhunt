state = []
def f(x):
    state.append(x)
    return x
x, y, z = 1, 2, 3
if f(x) < f(y) and f(y) < f(z):
    print(state)
else:
    print([0])
