obj = None
safe_dict = {'key': 'value'}
result = obj is not None and 'key' in obj.keys() or 'key' in safe_dict.keys()
print(f'Result: {result}')
