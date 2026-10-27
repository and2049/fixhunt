funcs = []
for i in range(2):
    mapping = {'a': i, 'b': i*2}  # b unused
    if (s := mapping.get('a')) is not None:
        funcs.append(lambda m=mapping: '%(a)s' % m)  # uses mapping
for f in funcs:
    print('Closure result:', f())
