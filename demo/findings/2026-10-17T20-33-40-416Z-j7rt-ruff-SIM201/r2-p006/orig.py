a = 0
b = 1
x = not a == b
print(f'not a == b -> {x!r} (type {type(x).__name__})')
if x:
    print('branch taken')
else:
    print('branch not taken')

y = a != b
print(f'a != b -> {y!r} (type {type(y).__name__})')
if y:
    print('branch taken')
else:
    print('branch not taken')
