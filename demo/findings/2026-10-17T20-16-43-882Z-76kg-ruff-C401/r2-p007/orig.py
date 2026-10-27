# This line triggers C401: set((y := x) for x in [1])
s = set((y := x) for x in [1])
try:
    print(y)
except NameError as e:
    print(f"NameError: {e}")
