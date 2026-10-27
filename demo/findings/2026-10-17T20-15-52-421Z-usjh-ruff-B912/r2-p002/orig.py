def func(a, b, **kwargs):
    return a + b
args = [(1, 2)]
kwargss = [{}]
try:
    result = list(map(func, *args, *zip(*[(1,2)], **{'strict': False})))
    print(result)
except TypeError as e:
    print(type(e).__name__, str(e))
