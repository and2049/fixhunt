def f():
    try:
        return 42
    finally:
        raise RuntimeError('finally wins')
try:
    f()
except Exception as e:
    print(type(e).__name__, str(e))
