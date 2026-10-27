def f(x=[]):
    x.append(1)
    pass  # Rule triggers: removable pass after stmt
    return x
print(f())
print(f())
print(f([]))
