def f(a, *, b=[]):
    b.append(a)
    return b[:]
try:
    res = list(map(f, [1, 2], * [[], []]))
except Exception as e:
    print('error:', type(e).__name__, str(e))
else:
    print('lists:', res)
