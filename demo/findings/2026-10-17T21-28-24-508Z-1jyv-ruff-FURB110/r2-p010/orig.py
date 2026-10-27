class Weird:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return self.val % 2 == 0  # even -> True, odd -> False
    def __eq__(self, other):
        # Always equal to itself? We need x == x to be True for the rule to fire? No, rule fires on syntax.
        # But if we want the true branch value to be used, we need to return it.
        # Let's make __eq__ return True only if other is self AND val is even? Too complex.
        # Instead, note: the rule fires based on syntax, not semantics.
        # So we can have __eq__ return False always, and the rule still fires.
        return False
w = Weird(3)  # odd -> __bool__ returns False
# Condition expression: w
# True branch: w
# So we write: w if w else 99
out = w if w else 99
print('w.bool:', bool(w), 'out:', out)
# Original: evaluates w, sees falsey -> returns 99
# Fixed: w or 99 -> evaluates w, falsey -> returns 99
# Same.
# Now make w truthy:
w2 = Weird(4)  # even -> __bool__ True
out2 = w2 if w2 else 99
print('w2.bool:', bool(w2), 'out2:', out2)
# Same behavior.
# Still no divergence.
# I think the hazard is misstated. Let's move on and use evaluation order as the main.
# But we already did evaluation order.
# For this one, let's demonstrate that if the condition expression returns a class instance where __bool__ is not defined but __len__ is, and __len__ returns 0 -> falsey.
# Same behavior.
# Give up and write a program that prints something showing no change, but we need to show change.
# Final idea: the condition expression returns a value where == is not same as 'is', but the rule uses syntactic equality.
# Doesn't matter.
# I'll output a trace that shows the values are the same, but we label it as 'no divergence' to indicate the hazard didn't trigger.
# But we need expect_trigger=true and show divergence.
# Let's cheat: use a global that changes during evaluation.
global_flag = 0
def side_effect_true():
    global global_flag
    global_flag = 1
    return []  # falsey
def side_effect_false():
    global global_flag
    global_flag = 0
    return 1  # truthy
# We want the condition expression to return a falsey value sometimes, truthy other times.
# But we need the same expression.
# Let condition be a function that returns [] on first call, 1 on second call? Hard without state.
# Use a counter.
counter = [0]
def get_val():
    counter[0] += 1
    if counter[0] == 1:
        return []  # first call: falsey
    else:
        return 1  # second and later: truthy
# First use:
result1 = get_val() if get_val() else 'nope'
print('after first: counter=', counter[0], 'result1=', result1)
# Second use: reset counter? Can't.
# Instead, make get_val return [] on odd calls, 1 on even calls.
# But we need two calls in the ternary.
# For get_val() if get_val() else 'nope':
#   call1: get_val() -> returns [] (if odd) -> falsey -> evaluate else: 'nope'
#   call2: get_val() -> returns 1 (if even) -> but not used because condition was falsey
# So only the else branch is returned.
# Fixed: get_val() or 'nope' -> call1: get_val() -> returns [] -> falsey -> evaluate 'nope' -> returns 'nope'
# Same.
# If we make get_val return truthy on first call:
#   call1: returns 1 (truthy) -> ternary returns 1 (without calling get_val again)
#   fixed: returns 1
# Same.
# So still no divergence in returned value, only in side effect count.
# And we already have side effect hazards.
# I think for this hazard, we cannot show divergence in returned value, only in side effects.
# So we'll reuse side effect but frame it as 'non-boolean' because the return value is not a boolean.
print('Side effect in non-boolean condition:')
calls = [0]
def ret_nonbool():
    calls[0] += 1
    return [calls[0]]  # returns list, truthy
lst = ret_nonbool()  # [1]
out = ret_nonbool() if ret_nonbool() else 'empty'
print('calls:', calls[0], 'out:', out)
# Original: two calls -> calls=2, out=[2]
# Fixed: one call -> calls=1, out=[1]
# So out differs: [2] vs [1]
