def gen():
    for i in range(3):
        yield i

s = set()
g = gen()
s.update(g)
print(f'After first loop: {s}')
# Reuse generator - now empty
s.update(g)
print(f'After second loop: {s}')
