def get_x():
    raise ValueError('bad')

try:
    if get_x() is not None:
        pass
except ValueError as e:
    print('Caught:', type(e).__name__, str(e))
