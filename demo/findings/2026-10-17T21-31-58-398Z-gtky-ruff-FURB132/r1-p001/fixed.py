def gen():
    yield 1
    yield 2
    yield 3
s = {1, 2, 3}
it = gen()
for _ in range(3):
    x = next(it)
    if x in s:
        s.remove(x)
print('Final set:', s)
