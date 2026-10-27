def f():
    print('side', end='')
    return 5
x = []
x.append(f())  # side effect happens before list append
print(''.join(x))
y = round(f(), 0)
print(y)
