try:
    raise (ValueError('error'))
except ValueError as e:
    print('Caught:', str(e))
else:
    print('No exception')
finally:
    print('Finally block')
