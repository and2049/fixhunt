s = '0b1010'
part = s[2:]  # This is used below
try:
    num = int(part, 2)  # Original form - rule does NOT fire here because no [2:] in int() call
    # We need the rule to fire, so make it:
    num = int(s[2:], 2)  # Rule fires
    part = s[2:]  # Still executed
    print('Num:', num, 'Part:', part)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
# After fix: int(s[2:], 2) becomes int(s, 0)
# But part = s[2:] is still there, so no break.
# To make it break, we need the slice to be inside the int() and nowhere else.
# But hazard says: "if the code relies on the slice operation to return a substring for other uses"
# So we must use the slice result elsewhere.
# Suppose:
part = s[2:]
num = int(part, 2)  # No slice in int -> rule silent
# Not triggering.
# Make it:
num = int(s[2:], 2)
part = s[2:]  # Dependency
print('Num:', num, 'Part:', part)
# After fix: becomes
# num = int(s, 0)
# part = s[2:]
# Still works.
# Unless part is used before being defined? No.
# Idea: if s is modified between slice and use.
# But fix doesn't move the slice.
# Final attempt: make the slice have side effects via property.
class SliceStr:
    def __init__(self, s):
        self.s = s
    def __getitem__(self, self, key):
        print('Slice called')
        return self.s[key]
    def startswith(self, prefix):
        return self.s.startswith(prefix)
s = SliceStr('0b1010')
part = None
try:
    num = int(s[2:], 2)  # Triggers slice, rule fires
    part = s[2:]  # Second slice
    print('Num:', num, 'Part set:', part)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
print('Part final:', part)
