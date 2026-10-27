data = [1, 2, 3]
if (tmp := data[::-1]) and tmp[0] == 3:
    print('matched', tmp)
else:
    print('no match')
