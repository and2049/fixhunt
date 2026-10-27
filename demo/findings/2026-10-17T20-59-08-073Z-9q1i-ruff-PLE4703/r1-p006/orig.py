def gen():
    yield from {1, 2}
g = gen()
s = set(g)
for x in s:
    s.discard(x)
print(len(s))
