print('--- Hazard 6: Boolean type change ---')
# round(True, 0) -> 1 (int)
# After fix: True (bool)
# Downstream: if code expects int for indexing, counting, etc.
# Example: using the result as an index in a tuple.
t = ('zero', 'one', 'two')
idx = round(True, 0)  # 1 -> t[1] = 'one'
print('Index result:', t[idx])
# After fix: idx = True -> t[True] -> True is 1 -> 'one' — same!
# Because bool is subclass of int.
# Not broken.
# Example: using in set — {1, True} has length 1 because 1==True.
# Still same.
# Example: using in dict key — {1: 'a', True: 'b'} -> {1: 'b'} because 1==True.
# Same.
# We need: an operation that distinguishes 1 and True.
# Example: type check.
if type(round(True, 0)) == int:
    print('Type is int')
else:
    print('Type is not int')
# After fix: type(True) == int? False -> prints 'Type is not int'
# Difference!
# Also: isinstance(round(True, 0), int) -> True
# isinstance(True, int) -> True — same.
# So we use explicit type() comparison.
print('type(round(True,0)):', type(round(True, 0)))
print('type(True):', type(True))
# Another: len([round(True, 0)]) -> 1
# But we want to see if the element is considered int for math.
# We do: sum([round(True, 0), round(True, 0)]) -> 2
# After fix: sum([True, True]) -> 2 — same.
# We use: the code does arithmetic that assumes the value is not a boolean for display.
# Or: we use the value in a format specifier that treats bool and int differently.
# No such specifier.
# We use: trying to convert to float via constructor that is explicit.
# But float(True) == 1.0.
# We use: the code catches OverflowError or something — no.
# Best: use the value in a context where the __int__ or __index__ method is expected, but bool inherits.
# We give up and use the type() check — it shows a difference.
# We also show a case where the value is used in a bytearray constructor.
try:
    b = bytearray(round(True, 0))  # bytearray(1) -> bytearray(b'\x00')
except Exception as e:
    print('bytearray(round(True,0)) error:', type(e).__name__, str(e))
try:
    b = bytearray(True)  # bytearray(True) -> TypeError: integer required, got bool
    # Actually: bytearray(True) works? Let's check: bool is subclass of int -> yes.
    # In Python: bytearray(True) -> bytearray(b'\x00')
    # So no error.
except Exception as e:
    print('bytearray(True) error:', type(e).__name__, str(e))
# Both work.
# We use: memoryview
try:
    mv = memoryview(bytearray(round(True, 0)))
    print('memoryview len:', len(mv))
except Exception as e:
    print('memoryview error:', type(e).__name__, str(e))
try:
    mv = memoryview(bytearray(True))
    print('memoryview len:', len(mv))
except Exception as e:
    print('memoryview error:', type(e).__name__, str(e))
# Same.
# Final: we use the type check and also show that in a list, the element repr differs.
print('List with one element:')
print('[round(True, 0)]:', [round(True, 0)])
print('[True]:', [True])
# Output: [1] vs [True] — visibly different.
