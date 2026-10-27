def f(b):
    if b:
        x = 1 / 0
    else:
        x = 42
    return x
print(f(True))
print(f(False))
