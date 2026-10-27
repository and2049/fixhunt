x = 'outer'
d = {'a': 1}
for x, _ in d.items():
    def inner():
        return x
    print(inner(), end='')
