# Walrus in comprehension: target leaks in list comp scope (but not in set comp) in Py3.8+
# However, in function scope, neither leaks. Use class scope to see leak.
class ScopeTest:
    pass
# In class scope, list comprehension leaks walrus var; set comp does not.
# Rule rewrites set([...]) -> {...}, removing leak.
try:
    ScopeTest.walrus_var = None  # Initialize
    s = set([(ScopeTest.walrus_var := i) for i in [1, 2, 3]])
    print('After list-based set:', hasattr(ScopeTest, 'walrus_var'), ScopeTest.walrus_var)
except Exception as e:
    print('Error in list-based:', type(e).__name__, e)
try:
    ScopeTest.walrus_var = None  # Reset
    s2 = {(ScopeTest.walrus_var := i) for i in [1, 2, 3]}  # After fix
    print('After set-literal:', hasattr(ScopeTest, 'walrus_var'), ScopeTest.walrus_var)
except Exception as e:
    print('Error in set-literal:', type(e).__name__, e)
# Output: list-based leaks walrus_var=3; set-literal does not (or leaks? Actually, in class scope, set comp also leaks?)
# Correction: in class scope, both leak. Need function scope.
# Redo in function.
def test():
    walrus_var = None
    s = set([(walrus_var := i) for i in [1, 2, 3]])
    return walrus_var  # Unbound in Py3.8+ if leaked? Actually, list comp does NOT leak in function scope.
# Walrus never leaks in function scope comprehensions. So hazard is misstated.
# Actual hazard: walrus in condition? Use assignment expression in filter.
# Ref: https://stackoverflow.com/questions/52854790/assignment-expression-in-list-comprehension
# In function scope: walrus does NOT leak. So no hazard? But rule says "may prematurely end variable's scope"
# Perhaps: if walrus used AFTER set() call, and list comp kept it alive longer? No.
# Instead: make walrus bind a resource that needs cleanup; list comp holds ref longer via list.
class Resource:
    def __init__(self, id): self.id = id
    def __del__(self): print(f'Resource {self.id} cleaned')
def make_resources():
    for i in range(2):
        yield Resource(i)
gen = make_resources()
# List comp: holds full list in memory during set() call; resources live until set built.
# Set comp: resources may be freed earlier? Not guaranteed.
s1 = set([r for r in gen])  # List built first
print('After list-based set creation')
gen = make_resources()
s2 = {r for r in gen}      # Set comp
print('After set-literal creation')
# Print order of __del__ may differ.
