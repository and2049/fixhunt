def bad():
    raise ValueError('bad')
try:
    try:
        bin(bad()).count('1')
    except ValueError as e:
        raise RuntimeError('worse') from e
except RuntimeError as e:
    print(type(e).__name__, str(e))
    print(type(e.__cause__).__name__, str(e.__cause__) if e.__cause__ else None)
