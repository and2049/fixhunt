def f(x, lst=[]):
    lst.append(x)
    return lst
prefix = 'pre'
s = 'prefix'
if s.startswith(prefix):
    s = s[len(prefix):]
f(s)
print(f.__defaults__[0])
