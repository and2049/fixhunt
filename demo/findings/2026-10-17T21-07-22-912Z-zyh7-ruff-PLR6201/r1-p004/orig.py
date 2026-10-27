bad_key = [1, 2]
try:
    res_before = bad_key in [1, 2, 3]
    print(f'Before: {bad_key!r} in [1,2,3] -> {res_before}')
except Exception as e:
    print(f'Before error: {type(e).__name__}: {e}')
try:
    res_after = bad_key in {1, 2, 3}
    print(f'After:  {bad_key!r} in {{1,2,3}} -> {res_after}')
except Exception as e:
    print(f'After error:  {type(e).__name__}: {e}')
