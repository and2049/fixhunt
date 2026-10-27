def g(*, arg=[0]):
    arg.append(1)
    return arg
# Rule triggers on next line: checks if result contains first element
lst = g()
print(lst[0] in lst)  # before: True; after fix: compares lst[0] == lst[0]? still True but side effect changed
# To see difference, call again:
lst2 = g()
print(lst2[0] in lst2)  # now lst2 is [0,1,1]; lst2[0]==0; 0 in [0,1,1] -> True; 0 == lst2[0] -> True
# But we need behavioral diff -- use containment vs equality on mutated list
# Instead: test if the *same* list object is in a list of lists
container = [[0], [0,1]]
el = [0]
print(el in container)  # False
el.append(1)
print(el in container)  # True
# Not triggering rule. Let's do proper hazard.
# Redo: function with keyword default that mutates, and we test membership in that default.
def h(*, x=[]):
    x.append(1)
    return x
# Rule triggers: check if 0 in h()
print(0 in h())  # First call: h() returns [1]; 0 in [1] -> False
print(0 in h())  # Second: [1,1]; still False
# No diff. Use identity.
print([] in [h()])  # First: [[]] in [[1]]? False; after fix: [] == h()[0]? [] == 1? False
# Still both False. Need where containment differs from equality.
# Use NaN.
import math
nan = float('nan')
print(nan in [nan])  # True
print(nan == nan)   # False
# Rule would trigger on nan in [nan] -> rewrite to nan == nan -> changes True to False
print(nan in [nan])  # Expected True
try:
    print(nan == nan)
except Exception as e:
    print(type(e).__name__, e)
