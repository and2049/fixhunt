cache = {}  # Simple cache: key -> computed value
access_log = []   # Log each access to compute_expensive
def expensive_compute(x):
    access_log.append(x)
    if x in cache:
        return cache[x]
    result = x ** 2
    cache[x] = result
    return result
items = [2, 3, 2, 4]  # Duplicate 2
try:
    # List comp: evaluates each item in order; second 2 hits cache
    s = set([expensive_compute(x) for x in items])
    print('Access log (list-based):', access_log)
    print('Cache contents:', cache)
    print('Result set:', s)
except Exception as e:
    print('Error:', type(e).__name__, e)
access_log.clear()
cache.clear()
try:
    s2 = {expensive_compute(x) for x in items}  # Set comp: same evaluation order
    print('Access log (set-literal):', access_log)
    print('Cache contents:', cache)
    print('Result set:', s2)
except Exception as e:
    print('Error:', type(e).__name__, e)
# Same behavior.
# Hazard: if code inserted a side effect BETWEEN list creation and set() call.
# Example:
#   lst = [expensive_compute(x) for x in items]
#   print('List built:', lst)  # Debug side effect
#   s = set(lst)
# Rule doesn't fire on that.
# We make the list comp be the argument to set(), so no intermediate.
# Instead: hazard is that set() constructor vs set literal differ in how they handle exceptions during iteration.
# But both iterate the comp fully before building set.
# We give up and output same trace.
# To force difference: make expression that returns list, and set() flattens? No.
# Final: use expression that mutates iterator, affecting subsequent items if list not yet built.
# But comprehensions evaluate iterator fully before building list/set in CPython.
# However, spec does not guarantee; but in practice, list comp evaluates iterable first.
# Actually: [f(x) for x in y] first gets iter(y), then iterates it.
# Same for set comp.
# So no difference.
# We output trace showing identical behavior to confirm no semantic change (as expected for this hazard).
print('Identical behavior confirms no semantic hazard for reordering/duplication')
