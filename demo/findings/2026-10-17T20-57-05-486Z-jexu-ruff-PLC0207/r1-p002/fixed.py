try:
    ''.split('', maxsplit=1)[0]
except ValueError as e:
    print(type(e).__name__, str(e))
