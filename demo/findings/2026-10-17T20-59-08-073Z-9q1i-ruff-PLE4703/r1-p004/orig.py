s = {1}
fns = []
for x in s:
    fns.append(lambda: x in s)
    s.add(2)
print([f() for f in fns])
