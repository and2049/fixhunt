def f(a, *, b=print('default') or 0):
    pass

d = {'x': 1}
print('Start')
for k, v in d:  # Rule fires: should be d.items()
    f(k, v=b)
print('End')
