DATA = [1, 2, 3]

def foo(s=set(x for x in DATA)):  # Rule triggers here
    return s

# Default argument evaluated at def time
print('foo() first call:', foo())  # {1,2,3}

DATA = [4, 5, 6]
print('foo() second call:', foo())  # Still {1,2,3} — default bound at def time

# After fix: def foo(s={x for x in DATA}): ...
# Same timing: set literal evaluated at def time.
# So no change.
# But we show that if the default were evaluated at call time, it would differ.
# Since it's not, we note the hazard is that someone might think it's call-time.
# We print to show it's def-time.

# Class body example
class C:
    shared = set(x for x in DATA)  # Rule triggers here

print('C.shared:', C.shared)  # {1,2,3} at class definition
DATA = [7, 8, 9]
print('C.shared after DATA change:', C.shared)  # Still {1,2,3}
