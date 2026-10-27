import warnings
try:
    warnings.warn('error ahead')
    raise ValueError('failed')
except ValueError as e:
    print(f'Caught: {e}')
finally:
    print('Finally block executed')
