import typing
try:
    raise ValueError('bad')
except ValueError as e:
    print(f'Caught: {e}')
finally:
    print('finally runs')
    if False:
        raise RuntimeError('should not happen')
