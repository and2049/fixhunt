def f():
    yield 1
    yield 2

g = f()
lst = list(f())
a = len(g)
b = len(g)
c = len(lst)
d = len(lst)
print('gen len after int:', a, 'remaining:', b)
print('list len after int:', c, 'remaining:', d)
