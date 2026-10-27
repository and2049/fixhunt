def foo():
    """This function checks for None."""
    x = None  # input value
    if x is None:  # is it None? yes
        return 'null'
    return 'not null'
print(foo())
