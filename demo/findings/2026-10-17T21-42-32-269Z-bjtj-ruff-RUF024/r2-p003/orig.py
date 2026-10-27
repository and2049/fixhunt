def make_dict(*, keys, value=[]):
    return {k: value for k in keys}

# Before fix: dict.fromkeys(keys, [])
# After fix:  {k: [] for k in keys}  --> but here we use default arg
keys = ['a', 'b']
d1 = make_dict(keys=keys)
d2 = make_dict(keys=keys)
d1['a'].append(1)
print('d2["a"]:', d2['a'])  # Shared due to default
