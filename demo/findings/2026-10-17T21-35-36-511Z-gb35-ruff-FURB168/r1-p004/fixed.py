try:
    if 1 / 0 is None:
        print('unreachable')
    else:
        print('not none')
except ZeroDivisionError as e:
    print(f'{type(e).__name__}: {e}')
