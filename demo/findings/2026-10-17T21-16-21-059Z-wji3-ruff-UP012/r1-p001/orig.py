def f():
    str = type('S', (), {'encode': lambda self, *a: b'local'})()
    x = str.encode('utf-8')
    print(x)
f()
