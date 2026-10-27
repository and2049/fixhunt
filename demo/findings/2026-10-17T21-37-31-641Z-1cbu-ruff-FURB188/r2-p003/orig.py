x = 'hello'
pref = 'h'
if x.startswith(pref):
    x = x[len(pref):]
print(f'Result: {x!r}')
