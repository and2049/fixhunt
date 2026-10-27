s = {'hello', 'world'}
val = 'hello'
if val in s:
    s.remove(val)
print('Remaining:', ', '.join(s))
print('f-string: %s' % ', '.join(s))
print('format: {}'.format(', '.join(s)))
