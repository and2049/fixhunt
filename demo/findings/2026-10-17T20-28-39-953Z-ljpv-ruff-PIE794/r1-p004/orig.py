from contextlib import suppress
class C:
    cm = suppress(ValueError)
    cm.__enter__()
    cm = None
    try:
        cm.__exit__(None, None, None)
    except AttributeError as e:
        print(f'AttributeError: {e}')
