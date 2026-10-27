d = {'x': 0}
if d.get('x'):
    print('exists and truthy')
else:
    print(f"'x' in d: {'x' in d}, d['x']: {d['x']}")
