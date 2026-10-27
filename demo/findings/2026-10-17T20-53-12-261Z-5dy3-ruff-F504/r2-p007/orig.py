funcs = []
for i in range(2):
    if (data := {'a': i, 'unused': i*10}) is not None:
        template = '%(a)s'
        f = lambda: template % data
        funcs.append(f)
print('Results:', [f() for f in funcs])
