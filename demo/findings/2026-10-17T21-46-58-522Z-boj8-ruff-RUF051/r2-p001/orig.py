lst = [1]
dct = {}
try:
    if lst in dct: del dct[lst]
except Exception as e:
    print(f'{type(e).__name__}: {e}')
try:
    if lst in dct: del dct[lst]
except Exception as e:
    print(f'{type(e).__name__}: {e}')
