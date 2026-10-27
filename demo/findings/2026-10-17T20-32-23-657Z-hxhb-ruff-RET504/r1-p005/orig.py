def f():
    x = (yield 1)
    return x
g = f()
print(next(g))
try:
    g.send(2)
except StopIteration as e:
    print(e.value)
