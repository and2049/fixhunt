DEFAULT = []
def func(a, *, b=DEFAULT):
    if a is None:
        b.append(1)
        return b
    return b
print(func(None))
print(func(None))  # Shows mutable default accumulation
# If else removed, behavior unchanged, but rule still triggers
