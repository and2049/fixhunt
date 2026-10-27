print('--- Hazard 5: Lambda/comprehension ---')
# We show that removing round in a lambda changes the type of the value captured, which may affect optimizations.
# Even if semantics same, we show the trace differs via type.
f_lambda = lambda: round(True, 0)
print('Lambda result:', f_lambda(), type(f_lambda()))
# After fix: lambda: True
# Print: Lambda result: True <class 'bool'>
# Before fix: Lambda result: 1 <class 'int'>
# Difference in type.
# We also show in a comprehension.
numbers = [round(True, 0) for _ in range(2)]
print('List comp:', numbers, [type(x) for x in numbers])
# Before fix: [1, 1] -> [int, int]
# After fix: [True, True] -> [bool, bool]
# Print shows difference.
# We also make it have a side effect via a counter to show evaluation count.
counter = 0
def inc():
    global counter
    counter += 1
    return True

lam = lambda: round(inc(), 0)
comp = [round(inc(), 0) for _ in range(2)]
print('Lambda call:', lam())  # inc() called once -> counter=1
print('After lambda:', counter)
# Reset for comp
counter = 0
comp = [round(inc(), 0) for _ in range(2)]
print('List comp:', comp)
print('After comp:', counter)  # inc() called twice -> counter=2
# After fix:
# lam = lambda: inc()  # still calls inc() once
# comp = [inc() for _ in range(2)]  # still twice
# So evaluation count same.
# But the type of the values differs.
# We print the type of the results.
print('Lambda result type:', type(lam()))
print('List comp types:', [type(x) for x in comp])
