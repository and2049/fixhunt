class A:
    def vals(self): return []
class B(A):
    def vals(self, cache=[]):
        cache.append(super.vals())  # triggers rule: becomes super().vals()
        return cache
print(B().vals())  # First call: [ [] ]
print(B().vals())  # Second call: [ [], [] ] if super is B's super
# But if rule rewrites and super is shadowed?
# Let's add shadow after default is set:
shadow = super  # save original super
super = lambda: None  # shadow
# Now second call uses shadowed super
try:
    print(B().vals())  # super.vals() -> shadow().vals() -> None.vals() -> AttributeError
# But first call used original super (because default arg evaluated at def time)
# So: first print: [ [] ]
# second print: AttributeError
# If rule did NOT fire: first: [ [] ], second: super.vals() -> shadow.vals() -> AttributeError (same)
# Wait — need to see if rewrite changes behavior.
# Original: super.vals() -> calls A.vals() -> []
# Rewritten: super().vals() -> calls A.vals() -> [] (same!)
# So no difference unless super is not the built-in.
# Let's make super a class with vals that returns something else.
# Redefine:
class SuperMock:
    @staticmethod
    def vals(): return ["mock"]
super = SuperMock  # now super is a class
print('First:', B().vals())  # super.vals() -> SuperMock.vals() -> ['mock']
print('Second:', B().vals()) # cache now has [['mock']], then appends SuperMock.vals() -> ['mock'] -> [['mock'], ['mock']]
# If rule rewrote: super().vals() -> SuperMock().vals() -> but SuperMock has no instance vals -> AttributeError
# So:
# No rewrite: ['mock'] then [['mock'], ['mock']]
# With rewrite: First call: AttributeError on SuperMock().vals()
}
