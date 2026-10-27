def g(x, y=[]):
    y.append(1)
    return len(y)
try:
    a = g(0) and not g(0)
except:
    pass
print('y length after:', len(g(0, [])))
