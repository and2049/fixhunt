d = {'k': '%\n', 'v': '\t'}
k, v = zip(d.keys(), d.values())
s = ''.join(f'{a!r}:{b!r}' for a, b in k)
print(s)
