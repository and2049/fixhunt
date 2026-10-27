x = ['a', 'b']
tpl = tuple(x)
print(f'List result: {list(tpl)}')
print('Percent: %s' % list(tpl))
print('Format: {}'.format(list(tpl)))
s = "['%s']" % ','.join(list(tpl))
print(repr(s))
