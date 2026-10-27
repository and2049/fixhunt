def gen_keys():
    yield 'x'
    yield 'y'
k_iter = gen_keys()
container = {'x': 1, 'y': 2}
try:
    if next(k_iter) in container:
        del container[next(k_iter)]
except StopIteration:
    pass
print('remaining:', container)
print('exhausted:', list(gen_keys()))
