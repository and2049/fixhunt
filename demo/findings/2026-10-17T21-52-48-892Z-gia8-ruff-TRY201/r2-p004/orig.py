try:
    raise ValueError('x')
except (ValueError, TypeError) as exc:
    print('exc type:', type(exc).__name__)
    raise exc
print('after')
