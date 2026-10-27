list = []
list.append(1)
x = list
if x is not list:
    print('aliased')
else:
    print('same')
del list
