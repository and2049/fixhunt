def side():
    print('side')
    return True

if side() and (x == 1 or x == 2):
    print('taken')
else:
    print('skipped')
x = 1
