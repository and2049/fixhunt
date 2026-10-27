def f():
    if False:
        yield 1
    return None

try:
    list(f())
    print('no error')
except Exception as e:
    print(type(e).__name__, e)
