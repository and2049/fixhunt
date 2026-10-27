d = {'key': 'value'}
if 'key' in d:
    result = f"Nested: {'inner' if 'key' in d else 'outer'}"
else:
    result = "not found"
print(result)
