def gen():
    for i in range(4):
        yield i

g = gen()
s = set()
# first loop consumes gen
for x in g:
    s.add(x)
print('after first loop:', s)
# second loop sees empty
for x in g:
    s.discard(x)
print('after second loop:', s)
