d = {'k': '%\n', 'v': '\t'}
k, v = d.items()
s = ''.join(f'{a!r}:{b!r}' for a, b in k)
print(s)
