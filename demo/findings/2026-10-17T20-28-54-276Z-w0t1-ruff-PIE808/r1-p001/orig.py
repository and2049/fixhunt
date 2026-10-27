def make_checker(t):
    xs = []
    while (n := t) > 0:
        xs.append(lambda: [i for i in range(0, n)])
        t -= 1
    return xs[0]

f = make_checker(2)
print(f())
