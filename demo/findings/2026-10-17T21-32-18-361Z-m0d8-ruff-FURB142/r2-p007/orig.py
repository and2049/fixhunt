def gen():
    for i in range(3):
        yield i

s = set()
g = gen()
for x in g:
    s.add(x)
print(f'After first loop: {s}')
# Reuse generator - now empty
for x in g:
    s.add(x)
print(f'After second loop: {s}')
