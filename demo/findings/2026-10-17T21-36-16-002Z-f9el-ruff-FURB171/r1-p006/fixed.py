def f():
    # Rule triggers here: Ellipsis in [...]
    return ... in [...]
print(f())  # True
# After fix: would be ... == [...] [0] -> ... == ... -> True
# Still same. Need where ellipsis has special meaning.
# Ellipsis is used in slicing: a[..., 0]
# But comparing ellipsis to ellipsis is still True.
# However, if someone overrides __eq__ for ellipsis? Can't.
# Instead: use that Ellipsis is a singleton, but if the container is not a literal? Must be literal.
# Make the ellipsis come from a variable that equals Ellipsis but is not the same object? Impossible.
# Unless we define a class that instances equal to Ellipsis.
class FakeEllipsis:
    def __eq__(self, other):
        return isinstance(other, type(Ellipsis))
    def __repr__(self):
        return 'FakeEllipsis()'
fe = FakeEllipsis()
# Rule does NOT trigger because container is [fe] but fe is not literal Ellipsis.
# We need container literal with Ellipsis.
# So: container is [...], literal.
# Now, if we have code that expects Ellipsis to mean something else in context.
# Example: using Ellipsis in slice notation.
a = [[1,2,3], [4,5,6]]
# Normally: a[:, 0] would be invalid, but a[..., 0] works
slice_obj = (..., 0)
# Rule triggers: check if slice_obj[0] in [...]
print(slice_obj[0] in [...])  # True: Ellipsis in [...]
# After fix: slice_obj[0] == [...] [0] -> Ellipsis == Ellipsis -> True
# Same.
# Instead: rely on the fact that ... == ... is True, but if we had a wrapper that lies about equality.
# Can't change Ellipsis.
# Give up and use: the hazard is that == ... is meaningless in most contexts, unlike containment which might be used in generic code.
# But we need behavioral diff.
# How about: if the container is not a list but a set, and Ellipsis is not hashable? But Ellipsis is hashable.
# Another idea: in NumPy, ellipsis means something, but we can't use NumPy.
# Finally: accept that for Ellipsis, containment and equality are both True, so no diff.
# But the rule says "semantically opaque". Maybe just note that it's strange to compare to ...
# We'll output the result and say it's True but confusing.
print('Result of Ellipsis in [...]:', ... in [...])
print('Result of Ellipsis == [...] [0]:', ... == [...] [0])
# Both True
