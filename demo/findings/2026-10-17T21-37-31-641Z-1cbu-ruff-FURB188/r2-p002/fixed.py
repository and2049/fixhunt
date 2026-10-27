def f(x, lst=[]):
    lst.append(x)
    return lst
prefix = 'pre'
s = 'prefix'
s = s.removeprefix(prefix)
f(s)
print(f.__defaults__[0])
