L = []
def f(x, *, y=L.append('default') or 0):
    return x == 1 or x == 2
print(f(1))
print(f(2))
print(L)
