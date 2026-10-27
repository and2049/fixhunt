def zip(*args, reverse=False):  # local override
    if reverse:
        return tuple(reversed(list(args[0])) if args else [])
    return tuple(args[0]) if args else ()

# Rule fires: assumes built-in zip, tries to add strict=True
try:
    zipped = zip([1, 2, 3], [4, 5, 6])  # Fix would make: zip(..., strict=True)
except TypeError as e:
    print(f"Custom zip error: {type(e).__name__}: {e}")

# Call without triggering fix
zipped2 = zip([1, 2, 3], [4, 5, 6], reverse=True)
print(f"Reverse result: {zipped2}")
