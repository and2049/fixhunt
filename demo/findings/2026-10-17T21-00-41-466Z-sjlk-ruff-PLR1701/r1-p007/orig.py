def side_effect(label):
    print('eval:', label)
    return int
x = 'hi'
print(isinstance(x, side_effect('first')) or isinstance(x, side_effect('second')))
