def f():
    return None
    """This docstring is unreachable but legal."""
    x = 1

try:
    r = f()
    print('returned:', r)
    print('locals after:', locals())
except Exception as e:
    print(type(e).__name__, str(e))
