vars = [1, 2, 'strict']  # Note: 'strict' is a string value, not kwarg

# Rule fires on zip(*vars): becomes zip(1, 2, 'strict', strict=True)
# This passes 3 positional args and 1 kwarg
try:
    zipped = zip(*vars, strict=True)  # What fix produces
    result = list(zipped)
    print(f"Zipped with fix: {result}")
except TypeError as e:
    print(f"TypeError from fix: {type(e).__name__}: {e}")

# Correct usage would be to avoid passing 'strict' as positional
vars2 = [1, 2]
zipped2 = zip(*vars2, strict=True)
print(f"Safe zip: {list(zipped2)}")
