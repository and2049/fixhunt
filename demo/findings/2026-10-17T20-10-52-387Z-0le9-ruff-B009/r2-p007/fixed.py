def process():
    """Process data."""
    obj = type('Obj', (), {'data': [1,2,3]})()
    # Retrieve data attribute
    return obj.data  # This comment explains the retrieval
print(len(process()))  # Should be 3
# After fix: return obj.data  # This comment explains the retrieval
# The comment is still there? Actually, Ruff's fix keeps trailing comments? Documentation says it does not.
# We assume it drops it. But again, no runtime effect.
# Same issue as hazard 6.
# We'll instead make the comment be part of a decorator via line number? No.
# Let's use the fact that the comment might be intended to cancel a warning on the next line.
# Example:
# # noqa: B009
# getattr(obj, "x")
# If fix removes getattr but leaves the noqa, it now applies to next line.
# But B009 is the rule we're fixing, so after fix there is no B009 trigger.
# However, if the comment was for another rule, say:
# # noqa: B001
# getattr(obj, "x")
# After fix, the noqa is now on a blank line or attaches to nothing, or to next line.
# We can show that if the next line has a violation, it is no longer suppressed.
import sys
# noqa: B001
obj = type('Obj', (), {'x': 1})()
# Now a line that would trigger B001 (blank line with whitespace?)\n# Actually B001 is about empty lines at module level.
# Let's use a fake rule: we'll define our own linter via ast? No.
# Given time, we'll output a program where we print whether a comment is present by checking __doc__ of a function? Not related.
# We'll do:
def f():
    # This comment should stay near the getattr
    obj = type('Obj', (), {'y': 2})()
    return obj.y
print(f().__doc__)  # None, not helpful
# We'll instead have the comment be a string that we concatenate and eval? Too risky.
# We'll output and note the limitation.
obj = type('Obj', (), {'attr': 'value'})()
result = obj.attr  # keep this comment
print(result)
# After fix: result = obj.attr  # keep this comment
# Behavior same.
