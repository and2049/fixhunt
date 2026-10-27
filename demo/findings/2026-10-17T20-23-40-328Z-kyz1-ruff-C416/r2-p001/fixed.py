data = [[1], [2]]
try:
    result = {x for x in data}
except Exception as e:
    print(f'comprehension error: {type(e).__name__}: {e}')
else:
    print(f'comprehension success: {result}')
data = [[1], [2]]
try:
    result = set(data)
except Exception as e:
    print(f'set() error: {type(e).__name__}: {e}')
else:
    print(f'set() success: {result}')
