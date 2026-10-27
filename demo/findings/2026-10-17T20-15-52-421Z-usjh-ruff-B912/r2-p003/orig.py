defaults = []
def kwonly_func(a, *, b=defaults.append(len(defaults)) or 10):
    return a + b
args = [[1], [2]]
try:
    res = list(map(kwonly_func, *args))
    print('result:', res)
    print('defaults:', defaults)
except Exception as e:
    print(type(e).__name__, str(e))
