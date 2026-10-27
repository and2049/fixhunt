d = {}
v = d.get('x')
s = '%r %s' % (v, v)
print(s)
t = '{!r} {!s}'.format(v, v)
print(t)
f = f'{v!r} {v!s}'
print(f)
