try:
    raise RuntimeError('fail')
except RuntimeError as e:
    print('Caught:', e)
    print('Type:', type(e))
