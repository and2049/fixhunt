def fmt(k): return f'id-{k}'
data = {'id-A': 10, 'id-B': 20}
k = 'A'
key_expr = fmt(k)
if key_expr in data:
    val = data.pop(key_expr, None)
    print(f'popped {key_expr} -> {val}')
print('remaining:', data)
