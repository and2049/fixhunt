def gen():
    for i in range(3):
        yield i
g = gen()
if True:
    for x in g:
        print(x, end='')
else:
    pass
print('
second:', list(gen()))
