def f():
    global a
    global b
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        b = 42
        raise RuntimeError('failed') from e
    else:
        b = 99
    finally:
        a = -1
try:
    f()
except RuntimeError as e:
    print('caught:', type(e).__name__, str(e))
    print('cause:', type(e.__cause__).__name__ if e.__cause__ else None)
    print('a=', a, 'b=', b)
