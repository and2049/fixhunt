def f(x=[]):
    x.append('a')
    return x
print(f())
print(f())
def g(y=[]):
    y.append('b')
    return y
g()
print(g())
