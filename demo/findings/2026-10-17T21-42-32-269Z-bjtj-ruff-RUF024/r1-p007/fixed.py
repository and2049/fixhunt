keys = ['a','a','b']
d1 = dict.fromkeys(keys, [])
d2 = {k: [] for k in keys}
print('fromkeys keys:', list(d1.keys()))
print('comp keys:', list(d2.keys()))
