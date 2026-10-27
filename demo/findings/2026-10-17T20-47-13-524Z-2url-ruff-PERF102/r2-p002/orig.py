d = {'a': 1, 'b': 2}
seen = []
for k, v in d.items():
    seen.append((k, v))
    if k == 'a':
        d['c'] = 3
print(sorted(seen))
