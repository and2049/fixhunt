def f():
    print('f called')
    return False
def g():
    print('g called')
    return True
def h():
    print('h called')
    return True
x = f() or (g() and h())
print(x)
