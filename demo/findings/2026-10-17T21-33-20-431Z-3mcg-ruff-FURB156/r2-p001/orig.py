try:
    if 'x' in '0123456789':
        raise ValueError('found')
except ValueError as e:
    print('caught:', e)
else:
    print('no error')
finally:
    print('cleanup')
