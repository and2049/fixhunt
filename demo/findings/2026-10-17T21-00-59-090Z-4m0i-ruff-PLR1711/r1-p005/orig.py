def f():
    def g():
        return 'escaped'
    x = g()
    y = x + ' more'
    return None
res = f()
print(res)
