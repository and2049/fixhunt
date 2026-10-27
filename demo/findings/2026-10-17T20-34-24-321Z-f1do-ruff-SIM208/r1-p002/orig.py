def f(x=[]):
    x.append(1)
    return x

def g():
    return f()

if not (not g()):
    print('first:', g())
else:
    print('unreachable')
print('second:', g())
