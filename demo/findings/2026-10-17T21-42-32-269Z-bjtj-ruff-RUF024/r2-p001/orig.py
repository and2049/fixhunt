def get_keys():
    print('get_keys called')
    return ['a', 'b']

# Before fix: dict.fromkeys(get_keys(), [])
# After fix:  {k: [] for k in get_keys()}
d = {k: [] for k in get_keys()}
print('Number of calls:', d.get('a', None) is not None and 1 or 0)
