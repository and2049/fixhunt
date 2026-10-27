d = {}
if True:
    d[(walrus := 1)] = 'inner'
print('walrus in outer?', 'walrus' in locals())
d = {}
if True:
    d[walrus := 1] = 'inner'
print('walrus in outer?', 'walrus' in locals())
