try:
    dict([([1, 2], 3)])
except TypeError as e:
    print('dict():', e)
try:
    {k: v for k, v in [([1, 2], 3)]}
except TypeError as e:
    print('{}:', e)
