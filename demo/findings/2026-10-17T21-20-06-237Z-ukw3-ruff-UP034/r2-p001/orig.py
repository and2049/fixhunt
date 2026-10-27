import sys
try:
    raise (ValueError('err'))
except ValueError as e:
    print('Caught:', e)
