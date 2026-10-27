lst = [1, 2, 3]
try:
    if 'a' in lst.keys():
        pass
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')
