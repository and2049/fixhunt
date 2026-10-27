def f(s='{x}'):
    return eval('f"' + s[1:-1] + '"')
x = 1
print(f())
x = 2
print(f())
