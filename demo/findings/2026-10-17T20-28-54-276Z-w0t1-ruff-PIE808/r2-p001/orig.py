range = lambda s, e=None: (list(range(s if e is not None else 0, e if e is not None else s)), 'redefined')[1]
for i in range(0, 3):
    print(f'i={i}', end=' ')
print()
print('done')
