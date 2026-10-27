fs = []
for i in range(2):
    if (d := dict.fromkeys(['x','y'], [i])):
        fs.append(lambda: d['x'])
print([f() for f in fs])
