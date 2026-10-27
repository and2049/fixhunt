i = 0
def next_i():
    global i
    i += 1
    return i
def f():
    if next_i() == 1:
        return next_i()
print(f())
