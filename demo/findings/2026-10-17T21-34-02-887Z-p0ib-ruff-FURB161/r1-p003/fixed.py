vals = []
for i in range(2):
    vals.append((lambda: [x for j in range(1) if (x := i + j) and bin(x).count('1')])())
print(vals)
# After fix: same behavior, walrus scoped correctly
