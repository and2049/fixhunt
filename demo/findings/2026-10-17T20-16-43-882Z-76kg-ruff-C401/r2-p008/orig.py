side_effects = []

def f():
    side_effects.append(len(side_effects))
    return [side_effects[-1]]

# This line triggers C401: set(x for x in f() for _ in [0])
s = set(x for x in f() for _ in [0])
print(f"Side effects: {side_effects}, set: {s}")
