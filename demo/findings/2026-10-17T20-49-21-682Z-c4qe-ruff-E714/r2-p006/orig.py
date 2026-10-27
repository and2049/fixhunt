list = []
list.append(1)
x = list
if not x is list:
    print('aliased')
else:
    print('same')
del list
