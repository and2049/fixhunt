x = 5
# First check: int, then str
if isinstance(x, int)  # prefer int
   or isinstance(x, str):  # fallback
    print('matched')
else:
    print('unmatched')
