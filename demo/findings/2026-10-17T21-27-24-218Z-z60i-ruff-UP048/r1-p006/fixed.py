def make_gen():
    i = 0
    while True:
        if i >= 3:
            break
        yield i
        i += 1

g = make_gen()
first = list(g)
second = list(g)  # exhausted
print(len(first), len(second))
