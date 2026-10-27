class MyFloat(float):
    pass
def make_myfloat():
    return MyFloat(4.0)
v = make_myfloat()
r = round(v, 0)
print('r type:', type(r))
print('r is MyFloat:', isinstance(r, MyFloat))
s = r + 1
print('s:', s, type(s))
# After fix: r becomes v (MyFloat), s becomes v+1 (still MyFloat)
# But if rule replaces round(v,0) with v, and v is MyFloat, then s is still MyFloat — no change?
# Hazard: if code expects round() to return base float, but here it's MyFloat — rule doesn't change type.
# So we need: expr is int literal → replaced with int, but user expects float subclass.
# Let's change: expr is int literal, but we have a wrapper that expects float.
class ExpectFloat:
    def __init__(self, val):
        if not isinstance(val, float):
            raise TypeError('Expected float')
        self.val = val
try:
    obj = ExpectFloat(round(5, 0))  # round(5,0) -> 5 (int) -> fails!
except TypeError as e:
    print('Caught:', type(e).__name__, str(e))
# After fix: round(5,0) -> 5 (same) — still fails. Not showing difference.
# New approach: make expr evaluate to int, but round() in some Python versions returns float?
# In Python, round(int, 0) returns int. So no.
# Instead: make expr = 5.0 (float), but rule does NOT fire on 5.0 — it’s not integer-typed.
# So we need expr that IS integer-typed but user expects round() to return float.
# Impossible: round(integer, 0) returns integer in Python.
# Therefore, hazard 2 is theoretical — but we simulate by having code that checks type.
# We'll show: if expr is bool (True), round(True,0) returns 1 (int), but if replaced with True, it's bool.
# Save that for hazard 6.
# For hazard 2: use a float that is integer-valued, like 5.0 — but rule does NOT fire.
# So we violate requirement? No — we must use firing shape.
# Let’s use: round(5, 0) → fires, returns int.
# Code that expects float: maybe from C extension? Simulate.
def process_float(f):
    return f.hex()  # only floats have hex
try:
    result = process_float(round(5, 0))  # round(5,0)=5 (int) -> AttributeError
except AttributeError as e:
    print('AttributeError:', type(e).__name__, str(e))
# After fix: same thing — still int.
# No change. But we can say: if the user had a monkey-patched round that returns float subclass,
# but rule assumes static knowledge — so if round is overridden, rule doesn’t fire (expr not statically known).
# So we make expr statically known int, but user patched round to return float — rule still fires and breaks.
original_round = round
round = lambda x, ndigits=None: float(x) if ndigits == 0 else original_round(x, ndigits)
print('Patched round: round(5,0) ->', round(5,0), type(round(5,0)))
try:
    val = round(5, 0)
    print('val.hex():', val.hex())  # works because it's float
# Now, if rule fires: it sees round(5,0) and replaces with 5 (int) — but only if it thinks round is built-in!
# But the rule does NOT know round is overridden — it assumes built-in.
# So in static analysis, it sees: round(5,0) → 5 (int) and replaces.
# But at runtime, our round returns float.
# However, the fix is applied by the tool — it rewrites the source.
# So after fix: val = 5 (int)
# Then val.hex() fails.
# We simulate by showing both:
print('---')
print('If rule rewrites round(5,0) to 5:')
val_fixed = 5  # simulated after fix
print('val_fixed:', val_fixed, type(val_fixed))
try:
    print('val_fixed.hex():', val_fixed.hex())
except AttributeError as e:
    print('AttributeError:', type(e).__name__, str(e))
print('Actual runtime (with patched round):')
val_actual = round(5, 0)
print('val_actual:', val_actual, type(val_actual))
print('val_actual.hex():', val_actual.hex())
