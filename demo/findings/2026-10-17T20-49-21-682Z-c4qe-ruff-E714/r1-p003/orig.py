def get_x():
    raise ValueError('bad')

try:
    if not get_x() is None:
        pass
except ValueError as e:
    print('Caught:', type(e).__name__, str(e))
