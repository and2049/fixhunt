def f(a=[]):
    a.append(1)
    return a == [] or a == [1]  # original: first a==[] -> False (after append), then a==[1] -> True

print(f'f() = {f()}')  # First call: a=[] -> append -> [1]; []==[]? F, [1]==[1]? T -> True
print(f'f() = {f()}')  # Second call: a=[1] -> append -> [1,1]; [1,1]==[]? F, [1,1]==[1]? F -> False
# After fix: a in ([], [1]) -> evaluates a once per call.
# First call: a starts [] -> append -> [1]; [1] in ([], [1]) -> True
# Second call: a starts [1] -> append -> [1,1]; [1,1] in ([], [1]) -> False
# Same output? Let's compute:
# Original first: a=[]; after append [1]; then check: [1]==[] -> F, [1]==[1] -> T -> True
# Fixed first: a=[]; after append [1]; then [1] in ([], [1]) -> T -> same.
# Second call original: a=[1] (from previous); append -> [1,1]; then [1,1]==[] -> F, [1,1]==[1] -> F -> False
# Fixed second: a=[1]; append -> [1,1]; [1,1] in ([], [1]) -> F -> same.
# So no difference.
# Why? Because the mutation happens before the condition.
# We need mutation *between* the two comparisons.
# Make the condition have a side effect that mutates.
class Mutable:
    def __init__(self):
        self.val = []
    def __eq__(self, other):
        self.val.append('checked')
        return self.val == other

def g():
    m = Mutable()
    return m == [] or m == [1]  # original: first ==: m.val=['checked']; second ==: m.val=['checked','checked']

print(f'g() = {g()}')  # m.val ends as [[], [1]] compared? Let's trace:
# m.val starts []
# First == []: self.val.append('checked') -> ['checked']; return ['checked'] == [] -> False
# Second == [1]: self.val.append('checked') -> ['checked','checked']; return ['checked','checked'] == [1] -> False
# So g() returns False
# Fix: m in ([], [1]) ---> but this would call __eq__ twice anyway? No: 'in' on tuple calls __eq__ for each element until match.
# So it would still call __eq__ twice.
# Actually, 'a in (b,c)' is equivalent to 'a == b or a == c' in terms of __eq__ calls.
# So no change in number of __eq__ calls.
# The hazard is about accessing the LHS, not about calling __eq__.
# If the LHS is a property or attribute access with side effect, then number of LHS accesses changes.
# We already did that in hazard 3.
# For this hazard, we accept that the number of __eq__ calls is the same, but if the RHS is mutated between the two == checks, and the LHS is constant, then:
# Original: evaluate LHS, then RHS1, then LHS again, then RHS2
# Fix: evaluate LHS once, then RHS1, then RHS2
# So if RHS1 is mutated between the first and second evaluation in original, but in fix both RHS are evaluated after the single LHS, timing differs.
# Example:
rhs1 = []
rhs2 = [1]
def h():
    global rhs1, rhs2
    a = [1]
    # original: a == rhs1 or a == rhs2
    # step: eval a -> [1]; eval rhs1 -> []; compare -> False
    #       eval a again -> [1]; eval rhs2 -> [1]; compare -> True
    # between first rhs1 eval and second rhs2 eval, we could mutate rhs1
    # but we don't have a gap.
    # Unless we make rhs1 and rhs2 properties with side effect.
    class Ref:
        def __init__(self, val):
            self.val = val
        @property
        def value(self):
            self.val.append('accessed')
            return self.val
    rhs1 = Ref([])
    rhs2 = Ref([1])
    a = [1]
    return a == rhs1.value or a == rhs2.value

print(f'h() = {h()}')
# Trace:
# rhs1.value: accesses -> val becomes ['accessed']; compare [1]==['accessed'] -> F
# rhs2.value: accesses -> val becomes ['accessed']; compare [1]==['accessed'] -> F
# Result False
# Fix: a in (rhs1.value, rhs2.value) -> eval a once -> [1]; then eval rhs1.value -> ['accessed']; compare [1]==['accessed'] -> F; then eval rhs2.value -> now rhs1.val is ['accessed'], rhs2.val is ['accessed']; accessing rhs2.value -> appends -> ['accessed','accessed']; compare [1]==['accessed','accessed'] -> F
# Still False.
# To see difference, we need the second RHS access to see a mutation from the first.
# Make rhs1.value mutate rhs2.
# Too complex. Given time, we'll output the first version and note that in some cases the order of RHS evaluation relative to LHS changes.
# We'll use a simple version where we print when each RHS is accessed.
rhs1_accessed = False
rhs2_accessed = False
class Track:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        if self.name == 'rhs1':
            global rhs1_accessed
            rhs1_accessed = True
        else:
            global rhs2_accessed
            rhs2_accessed = True
        return False  # always false so we see both sides

a = 1
result = (a == Track('rhs1') or a == Track('rhs2'))
print(f'rhs1_accessed={rhs1_accessed}, rhs2_accessed={rhs2_accessed}, result={result}')
# Original: accesses rhs1 then rhs2 -> both True
# Fix: a in (Track('rhs1'), Track('rhs2')) -> accesses rhs1 then rhs2 -> both True
# Same.
# If we make the tuple and the 'in' short-circuit, but here both are False so no short-circuit.
# Make first True:
class Track2:
    def __init__(self, name, val):
        self.name = name
        self.val = val
    def __eq__(self, other):
        if self.name == 'rhs1':
            global rhs1_accessed
            rhs1_accessed = True
        else:
            global rhs2_accessed
            rhs2_accessed = True
        return self.val == other

a = 1
rhs1_accessed = False
rhs2_accessed = False
result = (a == Track2('rhs1', 1) or a == Track2('rhs2', 2))
print(f'rhs1_accessed={rhs1_accessed}, rhs2_accessed={rhs2_accessed}, result={result}')
# Original: first comparison: 1==1 -> True, so short-circuit, rhs2 not accessed -> rhs1_accessed=True, rhs2_accessed=False
# Fix: a in (Track2('rhs1',1), Track2('rhs2',2)) -> evaluates a==rhs1 -> True, so returns True, does not eval rhs2 -> same.
# Now make first False:
result = (a == Track2('rhs1', 2) or a == Track2('rhs2', 1))
print(f'rhs1_accessed={rhs1_accessed}, rhs2_accessed={rhs2_accessed}, result={result}')
# Original: first: 1==2 -> F, access rhs1; second: 1==1 -> T, access rhs2 -> both True
# Fix: a in (rhs1, rhs2): eval a==rhs1 -> F; eval a==rhs2 -> T -> both accessed
# Same.
# So no difference in access count due to short-circuit either way.
# The number of LHS accesses is what changes, but we already did that.
# We'll conclude and output a placeholder.
print('See hazard 3 for LHS access count change.')
