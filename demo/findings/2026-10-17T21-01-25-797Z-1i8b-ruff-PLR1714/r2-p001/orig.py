def gen():
    yield 1
    yield 2

g = gen()
a = []
for _ in range(2):
    if next(g) == 1 or next(g) == 2:
        a.append('yes')
    else:
        a.append('no')
print(a)
