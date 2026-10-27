def f():
    '''This is the docstring'''
    pass  # removal makes docstring the only stmt -> becomes __doc__
    return 42
print(f.__doc__, f())
