def f():
    def g():
        return 'escaped'
    x = g()
    y = x + ' more'
res = f()
print(res)
