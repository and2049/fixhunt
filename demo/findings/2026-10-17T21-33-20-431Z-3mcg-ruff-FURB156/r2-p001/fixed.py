import string
try:
    if 'x' in string.digits:
        raise ValueError('found')
except ValueError as e:
    print('caught:', e)
else:
    print('no error')
finally:
    print('cleanup')
