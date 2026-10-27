s = b'0b1010\n'
try:
    # Original: int(s[2:], 2) -> slices to b'1010\n' -> invalid for base 2
    result = int(s[2:], 2)
    print('Slice result:', result)
except Exception as e:
    print('Slice error:', type(e).__name__, str(e))
try:
    # Fix would produce: int(s, 0) -> b'0b1010\n' -> int ignores trailing whitespace? Yes, in Python.
    result2 = int(s, 0)
    print('Fixed result:', result2)
except Exception as e:
    print('Fixed error:', type(e).__name__, str(e))
# Show difference: if we remove newline first
s_clean = b'0b1010'
slice_clean = int(s_clean[2:], 2)
fixed_clean = int(s_clean, 0)
print('Clean slice:', slice_clean, 'fixed:', fixed_clean)
# Now with str version for comparison
s_str = '0b1010\n'
try:
    r1 = int(s_str[2:], 2)
    print('Str slice:', r1)
except Exception as e:
    print('Str slice error:', type(e).__name__, str(e))
try:
    r2 = int(s_str, 0)
    print('Str fixed:', r2)
except Exception as e:
    print('Str fixed error:', type(e).__name__, str(e))
