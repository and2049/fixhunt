lst = [1]
dct = {}
try:
    dct.pop(lst, None)
except Exception as e:
    print(f'{type(e).__name__}: {e}')
try:
    dct.pop(lst, None)
except Exception as e:
    print(f'{type(e).__name__}: {e}')
