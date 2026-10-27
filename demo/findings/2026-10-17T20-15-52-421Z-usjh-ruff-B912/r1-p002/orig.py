import sys
sys.modules[__name__].__all__ = ['x', 'y']  # side effect
x = [1, 2]
y = [3]
def g(a, b): return a + b
try:
    res = list(map(g, * [x, y]))
except Exception as e:
    print('error:', type(e).__name__, str(e))
else:
    print('sum:', sum(res))
