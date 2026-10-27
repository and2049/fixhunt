def f():
    if True:
        from builtins import str
    return str(42)
try:
    print(f())
except Exception as e:
    print(type(e).__name__, str(e))
