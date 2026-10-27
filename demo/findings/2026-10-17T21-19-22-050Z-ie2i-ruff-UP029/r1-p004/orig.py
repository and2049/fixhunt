try:
    from builtins import len
    x = len([1,2,3])
except NameError:
    x = 0
finally:
    print('finally', x)
