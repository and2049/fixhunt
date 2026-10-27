xs = [1, 2, 3]
results = []
for x in xs:
    if not (y := x * 2) == 4:
        results.append(y)
print(f'collected: {results}, last y: {y if 'y' in locals() else undefined}')

results2 = []
for x in xs:
    if (y := x * 2) != 4:
        results2.append(y)
print(f'collected2: {results2}, last y2: {y}')
