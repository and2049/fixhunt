import sys
T = (int, str)
def check(v):
    return isinstance(v, T) or isinstance(v, float)
x = [1]
try:
    r = check(x)
except Exception as e:
    print(f'{type(e).__name__}: {e}')
    sys.exit(0)
print(r)
