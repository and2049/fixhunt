def fmt(val):
    s = '%s' % val
    t = '{}{}'.format(s, '!')
    return None
r = fmt('A')
print(r)
s = fmt('B')
if s is None:
    print('got none')
