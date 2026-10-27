pop = lambda d, k=None: [None][0]
d = {'a': 1}
d.pop('a', None)
print('after del:', d)
if 'a' in d:
    pop(d, 'a')
print('after pop:', d)
