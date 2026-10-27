try:
    if isinstance(1/0, type(None)):
        print('unreachable')
    else:
        print('not none')
except ZeroDivisionError as e:
    print(f'{type(e).__name__}: {e}')
