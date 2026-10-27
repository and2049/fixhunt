def gen():
    yield 7
    yield 3
print(sum(bin(x).count('1') for x in gen()))
g = gen()
print(list(g))  # should be empty after first consumption
