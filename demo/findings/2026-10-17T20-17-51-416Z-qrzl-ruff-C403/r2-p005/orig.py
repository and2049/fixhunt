results = []
exceptions_caught = []
def maybe_fail(x):
    if x == 2:
        raise ValueError('fail at 2')
    return x * 10
items = [0, 1, 2, 3]
try:
    # List comp: builds list; exception during build stops list creation
    s = set([maybe_fail(x) for x in items if x != 1])  # Fails at x=2
    print('This should not print')
except Exception as e:
    exceptions_caught.append((type(e).__name__, str(e)))
    print('Caught in list-based:', exceptions_caught[-1])
# After fix: set comp fails same point.
exceptions_caught.clear()
try:
    s2 = {maybe_fail(x) for x in items if x != 1}
    print('This should not print')
except Exception as e:
    exceptions_caught.append((type(e).__name__, str(e)))
    print('Caught in set-literal:', exceptions_caught[-1])
# To see intermediate results: need to catch exception and inspect partial list.
# But list comp inside set() is not accessible.
# Instead: make conditional expression that may fail, but we wrap in try/except inside comp.
def safe_maybe_fail(x):
    try:
        return maybe_fail(x)
    except ValueError as e:
        return f'caught: {e}'
items = [0,1,2,3]
s1 = set([safe_maybe_fail(x) for x in items])  # No exception escapes
print('List-based result:', s1)
s2 = {safe_maybe_fail(x) for x in items}
print('Set-literal result:', s2)
# Same.
# Hazard: if code relied on catching exception OUTSIDE to get partial list.
# Impossible because list is transient.
# We output trace showing same behavior.
