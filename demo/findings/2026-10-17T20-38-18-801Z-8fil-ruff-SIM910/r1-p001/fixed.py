d = {'a': None, 'b': 1}
result = []
for k in ['a', 'b', 'c']:
    v = d.get(k)
    if v is None:
        result.append((k, 'missing_or_none'))
    else:
        result.append((k, 'present'))
print(result)
