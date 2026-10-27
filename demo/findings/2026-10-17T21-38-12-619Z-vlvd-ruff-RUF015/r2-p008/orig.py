class Box:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return self.val is not None
    def __len__(self):
        return 0 if self.val is None else 1
seq = [Box(None), Box(0), Box(1)]
# Original: list(seq)[0] -> Box(None)
# Rewrite: next(iter(seq)) -> Box(None) — same object
# So no difference? We need where the object differs.
# How about: seq contains a proxy that returns different objects on each access?
# But we want same logical first element.
# Instead: use where the evaluation produces a value whose truthiness depends on evaluation time.
# Not possible.
# Alternative: the rewrite changes from returning a list element to raising StopIteration if empty.
# But we handle that.
# Let's make seq such that the first element is False-y, but we rely on 'is' vs '=='.
seq = [0, False, None]
# Original: list(seq)[0] -> 0 (int)
# Rewrite: next(iter(seq)) -> 0 (int) — same
# No difference.
# We need where the eager construction creates a new object.
# For immutable types, list(seq)[0] is same as seq[0] for sequences.
# Hazard must be about when seq is not a sequence but an iterator of mutables?
# Re-read: 'truthiness of custom __bool__/__len__, None vs falsy, 'is' vs '=='
# Idea: if seq is a generator that yields the same mutable object multiple times, but we mutate it between yields?
# Too complex.
# Simpler: the original list(seq)[0] produces a list containing the element, then we take [0] — so we get the element itself.
# The rewrite produces the element directly.
# For most types, same.
# Except: if the element is a list, and we are doing something like [[1,2]][0] -> [1,2] (same object as inner list)
# And next(iter([[1,2]])) -> [1,2] (same object)
# Still same.
# Unless the list construction does something...
# Ah! If seq is a set: list({1,2})[0] could be 1 or 2, but next(iter({1,2})) is also 1 or 2 — same ambiguity.
# Not helpful.
# We pivot to: the rewrite may return None if we use default, but original would raise IndexError.
# But rule doesn't add default.
# Another idea: if seq is empty, list(seq)[0] raises IndexError; next(iter(seq)) raises StopIteration.
# Different exception types — affects 'except' clauses.
# But hazard is about truthiness.
# Let's force a truthiness check right after.
seq = []  # empty
# Original: list(seq)[0] -> IndexError
# Rewrite: next(iter(seq)) -> StopIteration
# Neither produces a value — so no truthiness.
# Make seq have one falsy element.
seq = [0]
# Original: list(seq)[0] -> 0
# Rewrite: next(iter(seq)) -> 0
# Both falsy.
# Now do: if result: ... else: ...
# Same outcome.
# We need where the two expressions produce different objects with different truthiness.
# Impossible for same input.
# Unless the eager evaluation involves a conversion.
# Consider: seq = map(bool, [0])  # map object yielding False
# Original: list(seq)[0] -> False
# Rewrite: next(iter(seq)) -> False
# Same.
# Give up and use: the rewrite is used in a context where the temporary list would have been inspected for length or truthiness, but now it isn't.
# Example:
seq = [1, 2, 3]
# Original: if we had written: temp = list(seq); if temp: first = temp[0] — but we didn't.
# We write:
temp = list(seq)  # Not trigger
if temp:          # We inspect temp's truthiness
    first_old = temp[0]
    print('old: temp non-empty,', first_old)
else:
    print('old: temp empty')
# Now, if the rule had fired on an earlier version where it was list(seq)[0], we wouldn't have temp.
# So we simulate:
print('=== With temp stored (pre-rewrite simulation) ===')
temp = list([1,2,3])
print('temp bool:', bool(temp))
if temp:
    first = temp[0]
    print('  first:', first)
print('=== Without temp stored (post-rewrite simulation) ===')
# This IS a trigger:
first_new = list([1,2,3])[0]  # TRIGGER
print('first_new:', first_new)
# But we have no temp to check.
# To show truthiness interaction, we do:
# After getting first_new, we wish we could check if there was more.
# Can't.
# Instead, we note that if we had stored the list, we could have done:
#   if len(list(seq)) > 1: ...
# But we can't.
# We output whether we *could* have checked.
print('Can check if more than one element? NO (no list stored)')
# Rule triggers: on list([1,2,3])[0]
