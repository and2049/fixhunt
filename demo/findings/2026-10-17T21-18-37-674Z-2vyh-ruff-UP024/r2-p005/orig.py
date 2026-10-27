def make_handler(*,
        exc_type=IOError,
        msg='default'):
    try:
        raise exc_type(msg)
    except exc_type as e:
        return f'handled {type(e).__name__}'
    except OSError as e:
        return f'OSError fallback {type(e).__name__}'
print(make_handler())
print(make_handler(exc_type=OSError))
