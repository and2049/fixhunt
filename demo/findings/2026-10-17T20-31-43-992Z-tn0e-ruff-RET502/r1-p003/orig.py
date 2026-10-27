def f(x):
    try:
        if x == 0:
            return 1/x
        return
    except ZeroDivisionError as e:
        print('caught:', e)
        return -1
    finally:
        print('finally')
print(f(0))
print(f(1))
