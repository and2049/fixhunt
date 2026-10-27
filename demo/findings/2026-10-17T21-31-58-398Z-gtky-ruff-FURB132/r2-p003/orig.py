counter = 0

def get_set():
    global counter
    counter += 1
    return {1, 2, 3}
s = get_set()
print('Initial counter:', counter)
counter = 0
if 1 in get_set():
    get_set().remove(1)
print('After if-remove calls:', counter)
counter = 0
# This simulates what the fix would do: one call to get_set
# But we can't run the fix, so we show the difference in evaluation
# Original: two calls to get_set() -> counter increases by 2
# Fixed: one call -> counter increases by 1
# We'll show by manually doing both
s1 = get_set()  # call 1
if 1 in s1:
    s2 = get_set()  # call 2
    s2.remove(1)
print('Two calls result:', counter)
counter = 0
s = get_set()   # call 1
if 1 in s:
    s.discard(1)  # no second call
print('One call result (simulated fix):', counter)
