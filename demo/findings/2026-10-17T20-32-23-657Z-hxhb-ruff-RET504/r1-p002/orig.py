def f():
    try:
        x = 1
    finally:
        x = 2
    return x
print(f())
