pop = lambda d, k=None: [None][0]
d = {'a': 1}
if 'a' in d:
    del d['a']
print('after del:', d)
if 'a' in d:
    pop(d, 'a')
print('after pop:', d)
