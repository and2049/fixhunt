def f(x=[]):
    x.append(1)
    return x

# This line triggers C401: set(item for item in f())
s = set(item for item in f())
print(f"After first call: {f()}")
s2 = set(item for item in f())
print(f"After second call: {f()}")
