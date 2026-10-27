try:
    1 / 0
except (ZeroDivisionError,) as e:  # handle division by zero
    print('caught:', type(e).__name__)
