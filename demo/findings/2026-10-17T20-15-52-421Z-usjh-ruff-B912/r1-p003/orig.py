x = [1, 2, 3]
def h(a, b): return a if a == b else 0
res = list(map(h, x, x))
print('all equal?', all(v == 1 for v in res))
