def f(*, template='Value: {x}'):
    return eval('f"' + template[1:-1] + '"')
x = 1
print(f())
x = 2
print(f())
