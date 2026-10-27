def f(x=[r'\_']):
    x[0] = 'changed'
    return x
print(f())
print(f())
s = [r'\_']
f(s)
print(s)
