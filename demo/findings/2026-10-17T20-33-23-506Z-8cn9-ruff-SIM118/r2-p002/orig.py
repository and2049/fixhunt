d = {'key': 'value'}
if 'key' in d.keys():
    result = f"Nested: {'inner' if 'key' in d.keys() else 'outer'}"
else:
    result = "not found"
print(result)
