def f():
    def g():
        return 5
    if True:
        return g()

print(f())
