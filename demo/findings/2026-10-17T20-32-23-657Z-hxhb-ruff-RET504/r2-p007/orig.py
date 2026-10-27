def f():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print('caught:', e)
        raise
    return x
try:
    f()
except ZeroDivisionError as e:
    print('re-raised:', e)
