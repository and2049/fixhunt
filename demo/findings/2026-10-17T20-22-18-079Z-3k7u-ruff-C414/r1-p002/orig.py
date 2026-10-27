if (t := tuple([1, 2, 3])):
    y = list(t)
    print(f'y: {y}, t: {t}')
else:
    print('unreachable')
# After fix: t is unbound
try:
    print(t)
except NameError as e:
    print(f'{type(e).__name__}: {e}')
