funcs = []
for i in range(2):
    if (s := u'value'+str(i)):  # u-prefix here
        funcs.append(lambda: s)
for f in funcs:
    print(f())
