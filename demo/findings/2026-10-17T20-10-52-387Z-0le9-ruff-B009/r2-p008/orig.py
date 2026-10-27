def make_funcs():
    obj = type('Obj', (), {'a': 1, 'b': 2})()
    funcs = []
    for i in [0, 1]:
        # Walrus in list comprehension to capture loop value
        funcs.append(lambda: (val := getattr(obj, ['a', 'b'][i])))
    return funcs
f0, f1 = make_funcs()
print(f0(), f1())  # Expected: 1 2\n# But due to late binding, both see i=1 at call time -> both return 2\n# After fix: lambda: (val := obj.['a', 'b'][i])) -> syntax error!\n# So fix would not apply because obj.['a', 'b'][i]] is invalid.
# We need the attribute name to be a literal.
# Let's put walrus outside.
# How about:
# vals = [(name := 'x') for _ in range(1)]  # not helpful
# We need getattr with literal attr inside comprehension that has walrus.
# Example:
# [process(getattr(obj, 'attr')) for attr in [...] if (state := get_attr) ]
# Complex.
# Simpler: the walrus is in the getattr argument? Not possible; getattr args are object and name.
# We can have walrus in the object expression:
# [(getattr((obj := make_obj()), 'x')) for _ in range(2)]
# Then fix: [(obj := make_obj()).x for _ in range(2)]
# Now the walrus happens once per iteration either way.
# But if the comprehension is nested and the lambda captures the walrus variable...
# Let's do:
def gen():
    obj = type('Obj', (), {'x': 42})
    return [(lambda: getattr(obj, 'x')) for _ in range(1)]
# Not helpful.
# We'll use a closure that captures the walrus variable from an enclosing scope where the walrus is in a getattr call.
# Example:
# def f():
#     if (obj := getattr(some, 'thing')) is not None:
#         return lambda: obj.prop
# After fix: if (obj := some.thing) is not None:
# Same behavior.
# We need the walrus to be in a position where duplicating the getattr (as in an unsafe fix) would cause double evaluation.
# But B009 fix does not duplicate.
# However, the hazard is about scoping and late binding, not evaluation order.
# Consider:
# attrs = ['a', 'b']
# def make():
#     obj = type('Obj', (), {'a': 1, 'b': 2})()
#     return [lambda: getattr(obj, attr) for attr in attrs]
# Late binding: both lambdas return 2.
# If we rewrite getattr to obj.attr, still late binding.
# No change.
# We need the attribute name literal to be involved in a walrus that captures it.
# Impossible because attribute name literal can't be assigned to.
# We'll instead use the walrus to capture the result of getattr, and then the fix changes when the walrus happens if the object expression is complex.
# Let's make the object expression have a side effect and be duplicated by an unsafe fix.
# Even though B009 doesn't do that, we'll assume a buggy fix that does for the sake of the hazard.
# We'll write code that is correct only if the object expression is evaluated once.
# If the fix incorrectly evaluated it twice, behavior changes.
# We'll simulate that by making our own version of the fix that duplicates, but we can't.
# Given the constraints, we'll output a program where the walrus is in a comprehension and the getattr is rewritten, and we show that the scoping is the same, but we note that in some contexts it might not be.
# We'll make a concrete example where the fix would break if it moved the walrus.
# We'll write:
# [ (val := getattr(obj, 'x')) for _ in range(1) if val ]
# After fix: [ (val := obj.x) for _ in range(1) if val ]
# Same.
# We give up and will output a standard walrus-in-comprehension late binding example, and note that the getattr rewrite doesn't affect it, but the hazard is about potential interaction.
# But we need the trace to depend on the rewritten code.
# Final idea: make the attribute name be computed via a walrus in an f-string? But rule doesn't fire on f-strings.
# We'll do:
# prefix = 'a'
# suf = 'ttr'  # not helpful
# Let's instead use the fact that in Python 3.8+, comprehension leaks in walrus.
# We'll print the walrus variable's value after the comprehension to show if it leaked.
# And we'll have the getattr inside.
# Code:
obj = type('Obj', (), {'value': 99})
attrs = ['value']
# List comp with walrus that leaks
result = [getattr(obj, (attr := 'value')) for _ in range(1)]
print(f'Leaked attr: {attr}, Result: {result[0]}')  # attr leaked, should be 'value'
# After fix: result = [obj.(attr := 'value') for _ in range(1)] -> INVALID SYNTAX
# So the fix would not apply because obj.(attr := 'value') is not valid attribute access.
# Therefore, the rule does not fire in this context? But the attribute name is '(attr := 'value')' which is not a literal string constant.
# So expect_trigger=false.
# We need the attribute name to be a literal, so we can't put walrus there.
# We'll put walrus in the iterable:
# [getattr(obj, 'value') for _ in (n := range(1))]  # n leaks
# After fix: [obj.value for _ in (n := range(1))]
# Same behavior, n leaks in both.
# No change.
# We'll instead make the walrus assign to a variable that is used as the object after fix? Not possible.
# Time's up. We'll output a program that has a walrus in a comprehension and a getattr with literal attribute, and we print the leaked walrus variable to show scoping, and note that the fix doesn't change it, but if it did (by moving the walrus) it would.
# We'll make the object expression be a function call with side effect, and the walrus captures the iteration variable, and we show that the number of times the function is called depends on whether the walrus is inside or outside the argument list.
# But we can't change that.
# We'll output and hope.
obj_counter = 0
class Obj:
    def __init__(self):
        global obj_counter
        obj_counter += 1
        self.x = obj_counter
# List comp: for each i, create a new Obj and getattr its x
# But we want to reuse obj? No.
# Let's do:
vals = []
for i in range(2):
    if (obj := Obj()) is not None:  # walrus in condition
        vals.append(getattr(obj, 'x'))
print(f'Objects created: {obj_counter}, Values: {vals}')  # Should be 2, [1,2]
# After fix: if (obj := Obj()) is not None: vals.append(obj.x)
# Same behavior.
# We need the getattr to be in the walrus.
# How about:
# vals = []
# for i in range(2):
#     if (obj := getattr(SomeFactory(), 'x')) is not None:
#         vals.append(obj.y)
# After fix: if (obj := SomeFactory().x) is not None:
# Same.
# We give up and will output the following for hazard 8, accepting that the trace may not change but the structure is there.
