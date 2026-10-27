ls = []
for i in range(2):
    ls.append(lambda: (j := i))
print([f() for f in ls])
