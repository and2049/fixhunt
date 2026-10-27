def risky():
    try:
        data = list((1, 2, 0))
        return 10 / data[2]
    except ZeroDivisionError as e:
        raise ValueError('bad divisor') from e
    else:
        print('No error')
    finally:
        print('Cleanup')
try:
    risky()
except ValueError as e:
    print('Caught:', e.__cause__.__class__.__name__, '-', e.__cause__)
