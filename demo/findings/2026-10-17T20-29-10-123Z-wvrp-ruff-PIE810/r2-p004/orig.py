parts = ['sun', 'moon', 'star']
results = []
for p in parts:
    if (s := p).startswith('s') or s.startswith('m'):
        results.append(s)
print('matched:', results)
