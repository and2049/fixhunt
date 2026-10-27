d = {'x': 0}
if 'x' in d and d['x']:
    print('exists and truthy')
else:
    print(f"'x' in d: {'x' in d}, d['x']: {d['x']}")
