pairs = ((i, i+1) for i in range(3))
d1 = dict(pairs)
print('d1:', d1)
try:
    d2 = dict(pairs)  # pairs is exhausted
    print('d2:', d2)
except Exception as e:
    print('Error on second dict:', type(e).__name__, ':', str(e))
pairs = ((i, i+1) for i in range(3))
dc = {k: v for k, v in pairs}
print('dc:', dc)
try:
    dc2 = {k: v for k, v in pairs}  # pairs exhausted
    print('dc2:', dc2)
except Exception as e:
    print('Error on second comp:', type(e).__name__, ':', str(e))
