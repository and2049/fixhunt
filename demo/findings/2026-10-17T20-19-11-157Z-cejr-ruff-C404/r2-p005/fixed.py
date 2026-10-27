def mutate_and_return_length(lst):
    lst.append((99, 99))
    return len(lst)
items = [(1, 2), (3, 4)]
lst_comp = [(x, y) for x, y in items]
print('mutate list result:', mutate_and_return_length(lst_comp))
print('final list:', lst_comp)
# Now with dict comp equivalent - but we pass a list!
# So we force a list build then convert? No - to test hazard we must pass the comp directly.
# Rewrite: if rule fires, it becomes dict comp -> we can't pass dict to mutate_and_return_length
# So we design: call site expects list, but rule changes it to dict comp -> type mismatch
# But we can't have both. Instead: store the comp result, then pass.
# Hazard: if the list's mutability was relied on after.
def g():
    r = [(x, x) for x in [1,2]]
    r.append((3,3))
    return len(r)
print('list mutability test:', g())
# If rule rewrote the comp to dict, this would fail - but it doesn't fire on assignment to r?
# It does: dict([(x,x) for x in [1,2]]) is the pattern. But here we don't wrap in dict().
# So make it:
h = dict([(x, x) for x in [1,2]])
print('h is:', type(h))
# Now, if we had passed the list comp to a mutator, but we didn't. Let's force:
items = [(1,2)]
b = list((x, x) for x in items)  # this is the list comp
print('b before mutate:', b, type(b))
mutate_and_return_length(b)
print('b after mutate:', b)
# Now the dict version that the rule would produce if we wrapped in dict():
# But we don't. So to test the hazard, we need a case where the list comp is used as a list.
# The hazard is: if someone passes the list comp (not wrapped) to a mutating function, and elsewhere
# there is a dict([...]) that gets rewritten, they are unrelated.
# So instead: make the list comp be the argument, and have a dict(...) nearby that gets rewritten.
# But they are separate. Unless we do:
#   f(dict([(x,x) for x in xs]))  and f expects a list? No.
# We need the dict(...) to be rewritten, and its result used where a list is expected.
# Impossible without type error.
# Refocus: hazard is when the list itself (the comp) is used where its list-ness matters.
# And there is a dict([comp]) that gets rewritten - but that's a different expression.
# So we accept that the hazard may not trigger a visible change unless the rewritten dict comp is
# used in a list-expecting context - which would break.
# Example:
xs = [1,2]
# This dict([...]) will be rewritten to {x:x for x in xs}
# But if we then try to use it as a list...
d = dict([(x, x) for x in xs])  # becomes dict comp
if hasattr(d, 'append'):  # will be False
    d.append((99,99))
else:
    print('dict has no append')
# Whereas if it stayed a list comp wrapped in dict(), it's still a dict.
# No difference.
# Give up and use the eval example from before but add mutation.
# Final decision: use a function that expects a list and mutates it, and pass the result of
# a dict([list_comp]) - but that makes no sense.
# Instead: the list comprehension itself is used elsewhere.
# Let me just output a coherent example for the next hazard and note this one is best-effort.
