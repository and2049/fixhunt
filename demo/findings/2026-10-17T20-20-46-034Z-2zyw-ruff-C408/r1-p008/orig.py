side = []
def f():
    side.append(1)
    return dict()
x = f()
side.append(2)
print(side, x)
