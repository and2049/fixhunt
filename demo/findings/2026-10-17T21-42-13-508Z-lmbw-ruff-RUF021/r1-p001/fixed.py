def f():
    print('f')
    return False
side = []
def g():
    side.append(1)
    return True
x = (f() and g()) or True
print(len(side))
x = (f() and g()) or True
print(len(side))
