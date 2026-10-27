funcs = []
for i in range(2):
    if (t := [(i, i+1)])[0]:
        funcs.append(lambda: t)
print([f() for f in funcs])
