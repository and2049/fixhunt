try:
    result = ''.split('', maxsplit=1)[0]
except ValueError as e:
    print('caught:', type(e).__name__)
finally:
    print('cleanup')
