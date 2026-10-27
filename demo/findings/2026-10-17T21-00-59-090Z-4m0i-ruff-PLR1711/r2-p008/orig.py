def f():
    """This is a docstring."""
    x = 1  # inline comment
    return x  # trailing comment

print(f.__doc__)
print(f())
