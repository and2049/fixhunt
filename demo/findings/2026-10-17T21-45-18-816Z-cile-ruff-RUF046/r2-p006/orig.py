def f(x=[]):
    x.append(1)
    return len(x)

print(f())
print(f())
