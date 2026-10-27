try:
    d = {list((1, 2)): 'ok'}
    print(d)
except TypeError as e:
    print(f'{type(e).__name__}: {e}')
