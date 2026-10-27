counter = 0
class T:
    def __init__(self): nonlocal counter; counter += 1

f = lambda x: isinstance(x, (T, int))
print(f(T()), counter)
counter = 0
print([f(T()) for _ in range(2)], counter)
