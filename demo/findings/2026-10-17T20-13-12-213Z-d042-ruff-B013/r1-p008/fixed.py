try:
    try:
        raise ValueError('first')
    except ValueError as e:
        raise RuntimeError('second') from e
except RuntimeError as e:
    print('Caught:', e)
    print('Cause:', type(e.__cause__).__name__ if e.__cause__ else None)
else:
    print('No exception')
finally:
    print('Finally ran')
