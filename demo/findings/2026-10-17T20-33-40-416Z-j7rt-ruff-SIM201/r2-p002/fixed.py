lst = [0]
if not lst == lst:
    print('unequal')
else:
    print('equal')

lst.append(1)
if not lst == lst:
    print('still unequal after append')
else:
    print('still equal after append')
