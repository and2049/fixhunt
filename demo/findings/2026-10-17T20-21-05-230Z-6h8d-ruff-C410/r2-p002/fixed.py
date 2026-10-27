def f(x=list([1, 2])):
    x.append(99)
    return x
print(f())
print(f())
