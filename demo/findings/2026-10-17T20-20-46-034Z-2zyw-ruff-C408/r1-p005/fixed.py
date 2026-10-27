fns = []
for i in range(2):
    if (x := list()) is not None:
        fns.append(lambda: len(x))
print([f() for f in fns])
