def gen():
    for i in range(0, 3):
        yield i
        print(f'yielded {i}')
g = gen()
print('first sum:', sum(g))
print('second sum:', sum(g))  # should be 0
