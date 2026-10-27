def f(l=[]):
    l.append(1)
    return  # explicit

a = f()
b = f()
print('returned a:', a)
print('returned b:', b)
print('default list:', f.__defaults__[0])
