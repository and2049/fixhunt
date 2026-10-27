range = lambda *a: list(__builtins__.range(*a))
x = range(0, 2)
print(x)
del range
x = range(0, 2)  # now built-in
print(list(x))
