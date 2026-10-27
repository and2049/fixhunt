def gen():
    for i in range(5):
        yield i
g = gen()
for x in list(g):
    if x == 2:
        break
    print('loop:', x)
print('remaining:', list(g))
