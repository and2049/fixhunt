def f():
    try:
        d = dict([(1, 2), (3, 1/0)])
    except ZeroDivisionError as e:
        print('caught:', type(e).__name__)
    else:
        print('no error')
    finally:
        print('finally')
f()
try:
    d = {(k, v) for k, v in [(1, 2), (3, 1/0)]}
except ZeroDivisionError as e:
    print('caught:', type(e).__name__)
else:
    print('no error')
finally:
    print('finally')
