obj = None
try:
    result = delattr(obj, 'nonexistent')
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')
else:
    print('No error:', result)
