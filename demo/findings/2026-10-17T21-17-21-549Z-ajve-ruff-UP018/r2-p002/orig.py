lst = []
if bool(lst):
    print('truthy')
else:
    print('falsy')
if lst:  # same as bool(lst) but different identity
    print('list truthy')
else:
    print('list falsy')
