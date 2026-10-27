def func(a, b=5, *, c=10):
    print(f'a={a}, b={b}, c={c}')
    return b + c

# Defaults are evaluated once at definition time.
# round(5,0) -> 5 (int)
# round(10,0) -> 10 (int)
# After fix: b=5, c=10 — same values.
# But if we rely on the fact that the default is the *result* of round, and round might have side effects — none.
# To see a difference, we need the default to be evaluated multiple times — but it’s not.
# Instead, we make the default depend on a mutable or changing state — but defaults are evaluated once.
# We’ll use a global that changes.
global_counter = 0
def get_counter():
    global global_counter
    global_counter += 1
    return global_counter

def func2(a, b=get_counter(), c=get_counter()):
    # This is invalid: non-default arg after default — syntax error.
    pass
# Correct way:
def func2(a, b=get_counter(), c=get_counter()):
    # b and c defaults evaluated at definition.
    print(f'b={b}, c={c}')
    return b + c

# First call: b=1, c=2
# Second call: b=1, c=2 (same)
# After fix: same.
# No difference.
# We need: the default expression is round(x,0) where x has side effects, and we want to see if removing round changes when the side effect happens.
# But default is evaluated once — so side effect happens once either way.
# Unless the rule removes the round call and the default becomes x — but if x has side effects, and the default is evaluated once, still one side effect.
# No difference.
# We make the default expression be used in the function body in a way that its value is used multiple times — but the default value is fixed.
# Example:
def func3(a, b=5):
    print(b)
    print(b)  # uses same value
# After fix: b=5 -> prints 5 twice.
# Same.
# We need: the default is supposed to be recomputed each call — but it’s not.
# So we cannot test that.
# Instead, we test: if the function is called without providing b, and the default is round(5,0), and inside the function we do something that depends on the type of b.
# But b is int either way.
# We use: the default expression is round(True, 0) -> 1 (int), but after fix it’s True (bool).
# Then inside function, we do: if b: ... — same truthiness.
# Or: b + 1 -> 2 either way.
# Or: [b] -> [1] vs [True].
# We print the list.
global_counter = 0

def get_val():
    global global_counter
    global_counter += 1
    return global_counter  # 1,2,3...

def func4(a, b=get_val()):
    # Default evaluated once at definition: b = get_val() -> 1 (first call to get_val)
    lst = [b] * 3
    print(f'func4: b={b}, list={lst}')
    return lst

print('First call:')
r1 = func4(0)
print('Second call:')
r2 = func4(0)
# r1 and r2 both have b=1 (from first get_val() call)
# lists: [1,1,1]
# After fix: same.
# No difference.
# We make the default expression be round(get_val(), 0) — and get_val has side effect.
# Default: b = round(get_val(), 0) -> get_val() called once -> returns 1 -> round(1,0)=1.
# After fix: b = get_val() -> same.
# Still one call.
# To get multiple evaluations, we need the default to be re-evaluated — impossible.
# We abandon and use: the function is called with b omitted, and we inspect the default value via func.__defaults__.
print('--- Hazard 4: Defaults ---')
def func5(a, b=5):
    return b

print('func5.__defaults__:', func5.__defaults__)
# Before fix: (5,)
# After fix: (5,) — same.
# But if we could see the expression — we can’t.
# We instead show that if the default were a boolean, the type in __defaults__ changes.
def func6(a, b=round(True, 0)):
    return b

print('func6.__defaults__:', func6.__defaults__)
# Before fix: (1,) -> int
# After fix: (True,) -> bool
# Print shows: (1,) vs (True,)
# This is visible!
# And round(True,0) is a firing shape.
# We’ll use that.
print('func6.__defaults__:', func6.__defaults__)
