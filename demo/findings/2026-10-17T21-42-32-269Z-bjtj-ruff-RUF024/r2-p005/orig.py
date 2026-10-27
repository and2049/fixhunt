keys = ['a', 'b']
# Before fix: d = dict.fromkeys(keys, [])  # all values same list
# After fix:  d = {k: [] for k in keys}  # each value different list
d = {k: [] for k in keys}
print('Same object?', d['a'] is d['b'])
d['a'].append(1)
print('d["b"]:', d['b'])  # Should be [] if fix applied
