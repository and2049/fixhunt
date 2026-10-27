funcs = []
for i in range(2):
    if (x := '') == '':
        funcs.append(lambda: print(x, sep=''))
for f in funcs:
    f()
