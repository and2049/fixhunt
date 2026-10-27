def example():
    """This docstring should stay attached to the function."""
    x = 1  # ruff: disable
    y = 2  # this comment explains y
    return x + y
print(f"Function docstring: {example.__doc__}")
