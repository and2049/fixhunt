a = [1, 2]
b = [3, 4]
z = zip(a, b)
d1 = {k: v for k, v in z}
print('len(d1):', len(d1))
try:
    d2 = {k: v for k, v in z}
except ValueError as e:
    print('second dict error:', type(e).__name__, str(e))
else:
    print('d2 len:', len(d2))
