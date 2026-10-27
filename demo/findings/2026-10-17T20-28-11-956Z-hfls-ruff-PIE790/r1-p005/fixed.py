def f():
    'This is a string literal'
    # Rule triggers: removable pass after string -> becomes docstring
    return 'body'
print(repr(f.__doc__))
print(f())
