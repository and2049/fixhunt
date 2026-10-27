value: "int" = "42"
print(f'Value: {value}, type: {type(value)}')
try:
    coerced = int(value)
    print(f'Coerced to int: {coerced}')
except Exception as e:
    print(f'Coercion failed: {type(e).__name__}: {e}')
