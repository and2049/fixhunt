d = {}
v = d.get('x', None)
s = '%r %s' % (v, v)
print(s)
t = '{!r} {!s}'.format(v, v)
print(t)
f = f'{v!r} {v!s}'
print(f)
