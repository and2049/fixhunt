try:
    gen = (1 / x for x in [0, 1, 2])
    result = list(gen)
except ZeroDivisionError as e:
    print('Caught:', type(e).__name__, e)
finally:
    print('finally')
