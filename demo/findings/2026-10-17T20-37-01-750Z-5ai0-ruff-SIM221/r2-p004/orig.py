called = []
def f():
    called.append('f')
    return 0
def g():
    called.append('g')
    return 1
result = (f() or g()) or not (f() or g())
print('result:', result, 'called:', called)
