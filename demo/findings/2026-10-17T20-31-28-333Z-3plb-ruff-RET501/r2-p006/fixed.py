def f():
    x = 0
    if (x := x + 1) > 0:
        return
    return

print(f())
