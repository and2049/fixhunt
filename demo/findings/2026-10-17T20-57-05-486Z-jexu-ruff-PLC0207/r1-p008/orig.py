try:
    result = ''.split('')[0]
except ValueError as e:
    print('caught:', type(e).__name__)
finally:
    print('cleanup')
