result = []
# This line triggers C401: set((y := x) for x in [1, 2])
s = set((y := x) for x in [1, 2])
result.append(y)
print(f"Captured y: {result[-1]}, set: {s}")
