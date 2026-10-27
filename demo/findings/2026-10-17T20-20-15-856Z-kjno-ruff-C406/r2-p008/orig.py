def gen():
    yield (1, 2)
    yield (3, 4)
g = gen()
d1 = dict(g)  # First consumption
print('d1:', d1)
try:
    d2 = dict(g)  # Second consumption - exhausted
    print('d2:', d2)
except Exception as e:
    print('error on second:', type(e).__name__, str(e))
