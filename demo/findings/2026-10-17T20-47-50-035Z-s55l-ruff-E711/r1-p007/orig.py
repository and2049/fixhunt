def gen():
    for i in [None, 1]:
        yield i
 g = gen()
print(list(x == None for x in g))
