results = []
for i in range(3):
    # Build inner list via comprehension
    inner = [not j in [0, 1, 2] for j in range(i+1)]
    results.append(sum(inner))
print(results)
