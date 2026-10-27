def gen():
    for i in range(4):
        yield i

g = gen()
s = set()
# first loop consumes gen
s.update(g)
print('after first loop:', s)
# second loop sees empty
s.difference_update(g)
print('after second loop:', s)
