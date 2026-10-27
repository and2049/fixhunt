data = [[1], [2]]
items = data
for t in [(tuple(items[0]),), (tuple(items[1]),)]:
    try:
        result = t in [(tuple(items[0]),), (tuple(items[1]),)]
        print(f'Before: {t} in list -> {result}')
    except Exception as e:
        print(f'Before error: {type(e).__name__}: {e}')
    try:
        result = t in {(tuple(items[0]),), (tuple(items[1]),)}
        print(f'After:  {t} in set -> {result}')
    except Exception as e:
        print(f'After error:  {type(e).__name__}: {e}')
