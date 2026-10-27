def f(a, /, b, *, c=0): return (a, b, c)
val = [1, 2]
d = {(f(*val))[():]}
print('before:', list(d))
def g(a, /, b, *, c=0): return (a, b, c)
val = [1, 2]
d = {g(*val)[()]}
print('after:', list(d))
