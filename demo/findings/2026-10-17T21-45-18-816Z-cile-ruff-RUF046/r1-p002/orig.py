def check_int(x):
    return isinstance(x, int) and not isinstance(x, bool)

v = int(True)
print('int(True) is int?', isinstance(v, int))
print('int(True) passes check_int?', check_int(v))
print('type(int(True)):', type(v))
