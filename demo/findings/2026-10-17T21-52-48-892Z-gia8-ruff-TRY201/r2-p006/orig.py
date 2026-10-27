def outer():
    exc = None
    try:
        try:
            raise ValueError('test')
        except ValueError as e:
            exc = e
            raise
    finally:
        if exc is not None:
            print('finally saw:', exc)
outer()
