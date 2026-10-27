def get_first_rev(x):
    return list(reversed(x))[0]
try:
    print(get_first_rev([1, 2, 3]))
except Exception as e:
    print(type(e).__name__, e)
