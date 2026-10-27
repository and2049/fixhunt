def f(x=['\_']):
    x[0] = 'changed'
    return x
print(f())
print(f())
s = ['\_']
f(s)
print(s)
