# Simulate module side effects via exec
code = '''
__all__ = ['A']
A = 1
B = 2
'''
exec(code, globals())
# Rule triggers: check if 'A' in __all__
print('A' in __all__)  # True
# After fix: 'A' == __all__[0] -> 'A' == 'A' -> True
# Same. Need where __all__ is not a list literal? But rule needs literal.
# Make __all__ built via side effect that we test later.
global_list = []
def side_effect():
    global_list.append('x')
    return global_list
# __all__ not involved. Use: if we could do from mod import *, but can't.
# Instead: use that __all__ affects what star-import sees, but we can't do star-import.
# Hazard: if module has side effect in __all__ assignment, and we reload.
# Since we can't reload, simulate: two phases.
phase1_all = ['A']
# Simulate importing * from a module with __all__ = phase1_all
locals_copy = {}
for name in phase1_all:
    locals_copy[name] = globals().get(name, None)
# Now change phase1_all
phase1_all.append('B')
# If we had done star-import earlier, we wouldn't get B.
# Rule triggers: checking membership in phase1_all during import simulation
print('B' in phase1_all)  # Now True
# After fix: 'B' == phase1_all[0] -> 'B' == 'A' -> False
# So if rule fired during first check, it'd have used wrong value.
# But we need the rule to fire on a literal. Make phase1_all a literal? Can't.
# Use: at point of rule firing, the container is a literal, but later mutated.
# Container must be literal for rule to fire. So:
print('B' in ['A'])  # Rule triggers here: literal ['A']
# At this point, evaluates to False
# After fix: 'B' == ['A'][0] -> 'B' == 'A' -> False
# Same. Need where mutation happens between two checks.
# Store the literal in a variable? No, rule only fires on literals.
# So: two literals, same content, but we mutate a variable named same? Not possible.
# Give up and use: the literal is evaluated each time, but if we could mutate it... we can't.
# Instead: hazard is that fixing to equality breaks if the item has side effect when accessed twice.
item = ['side']
class Side:
    def __eq__(self, other):
        print('EQ')
        return False
    def __hash__(self):
        return 0
s = Side()
print(s in [s])  # Rule triggers: calls __contains__ -> iterates, calls __eq__ once? Actually list.__contains__ does == for each item.
# So: iterates over [s], calls s.__eq__(s) -> prints EQ, returns ?
# After fix: s == [s][0] -> calls s.__eq__(s) again -> prints EQ again.
# So if we count EQ calls, differ.
counter = 0
class Side2:
    def __eq__(self, other):
        nonlocal counter
        counter += 1
        return other is self
    def __hash__(self):
        return id(self)
s2 = Side2()
print(s2 in [s2])  # Should trigger rule; counter +=1
print(f'EQ calls after in: {counter}')
counter = 0
print(s2 == [s2][0])  # After fix version; counter +=1
print(f'EQ calls after == : {counter}')
# Both 1. No diff.
# Need where __contains__ and == differ in side effects.
# For list, __contains__ is equivalent to any(x == e for x in self). So same number of == calls.
# Thus no side-effect difference for list.
# For other containers? Rule also fires on sets, etc.
# Set __contains__ uses hash, not == necessarily.
# So: if item has custom __hash__ that has side effect.
class Side3:
    def __hash__(self):
        print('HASH')
        return 1
    def __eq__(self, other):
        return self is other
s3 = Side3()
print(s3 in {s3})  # Rule triggers: set lookup -> calls __hash__ once
print('After in')
# After fix: s3 == {s3}.pop() -> but fix would be s3 == next(iter({s3})) -> still calls __eq__.
# And to get iterator, need to iterate set -> which may call __hash__ again.
# Actually: next(iter({s3})) will call __hash__ on s3 to get hash, then look in set.
# So: s3 in {s3}: calls __hash__ once
# s3 == next(iter({s3})): 
#   - next(iter({s3})): creates iterator, calls __hash__ to hash s3 for bucket, finds it, returns s3
#   - then s3 == s3: calls __eq__
# So: one __hash__ vs one __hash__ + one __eq__
# If __hash__ has side effect, count differs.
hash_counter = 0
eq_counter = 0
class Side4:
    def __hash__(self):
        nonlocal hash_counter
        hash_counter += 1
        return 1
    def __eq__(self, other):
        nonlocal eq_counter
        eq_counter += 1
        return self is other
s4 = Side4()
hash_counter = eq_counter = 0
print(s4 in {s4})  # should print HASH once
hash_after_in = hash_counter
eq_after_in = eq_counter
print(f'HASH after in: {hash_after_in}, EQ after in: {eq_after_in}')
hash_counter = eq_counter = 0
print(s4 == next(iter({s4})))  # HASH (for finding in set) + EQ
hash_after_eq = hash_counter
eq_after_eq = eq_counter
print(f'HASH after == : {hash_after_eq}, EQ after == : {eq_after_eq}')
# Expected: after in: HASH=1, EQ=0; after ==: HASH=1, EQ=1
# So EQ count differs.
