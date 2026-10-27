side_effects = []

def record(x):
    side_effects.append(x)
    return x

a = record(None)
b = record(None)
# This condition uses type(a) is type(None) in a compound expression
if type(a) is type(None) and type(b) is type(None):
    print('Both are None')
else:
    print('At least one is not None')
print('Side effects recorded:', side_effects)
# After fix: a is None and b is None
# Should still record two effects, but we're testing if the rule duplicates/deletes
