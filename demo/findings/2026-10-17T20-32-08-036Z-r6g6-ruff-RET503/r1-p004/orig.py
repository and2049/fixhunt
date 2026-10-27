def f():
    def inner():
        return 42
    if True:
        return inner()
print(f())
