def f(a=[]):
    a.append(1)
    return a
x = f()
if not x is f():
    print('different')
else:
    print('same')
print(id(x), id(f()))
