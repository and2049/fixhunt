def f(x=[]):
    x.append(1)
    return len(x)
a = f()
b = f() or not f()
print('a:', a, 'b:', b)
