def f():
    """Process input."""
    s = 'a b c'
    # keep first word
    first = s.split(maxsplit=1)[0]  # inline comment
    print(first)
f()
