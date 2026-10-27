# Suppression inside comprehension affects walrus capture
results = [(lambda: x)() for x in [1] if (tmp := 2) and True  # ruff: disable]
print(f"First result: {results[0] if results else 'none'}")
