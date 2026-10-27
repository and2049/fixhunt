default = []
def f(*, x=default):
    x.append(1)
    return x
print(f())
print(f())
