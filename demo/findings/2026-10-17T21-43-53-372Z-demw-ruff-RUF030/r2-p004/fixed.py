import io, sys
old = sys.stdout
sys.stdout = io.StringIO()
try:
    x = -1
    assert x >= 0, print('neg', flush=True)
except AssertionError as e:
    pass
finally:
    sys.stdout = old
print('stdout buffer:', sys.stdout.getvalue().strip())
