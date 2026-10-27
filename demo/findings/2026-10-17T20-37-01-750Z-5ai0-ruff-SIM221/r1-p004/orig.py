def f():
    try:
        raise ValueError('bad')
    except ValueError as e:
        print('caught:', e)
        raise RuntimeError('worse') from e

try:
    print(f() or not f())
except Exception as e:
    print(type(e).__name__ + ':', e)
