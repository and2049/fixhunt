fs = []
for i in range(2):
    if (x := sorted([i, 0])) is not None:
        fs.append(lambda: x)
print([f() for f in fs])
