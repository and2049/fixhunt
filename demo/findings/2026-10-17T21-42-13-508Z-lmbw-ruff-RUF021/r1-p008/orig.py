side = []
def log():
    side.append(1)
    return 0
def f(a=log() or True and False):
    return len(side)
print(f())
side = []
def g(a=(log() or True) and False):
    return len(side)
print(g())
