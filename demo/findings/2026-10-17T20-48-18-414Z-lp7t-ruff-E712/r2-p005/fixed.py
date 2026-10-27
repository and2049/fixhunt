x = True
print('x == True:', x == True)
print('x is True:', x is True)
print('bool(x):', bool(x))
# After fix, x == True becomes x, which is truthy
if x == True:
    print('Equal branch taken')
else:
    print('Equal branch skipped')
if x:
    print('Truth branch taken')
else:
    print('Truth branch skipped')
