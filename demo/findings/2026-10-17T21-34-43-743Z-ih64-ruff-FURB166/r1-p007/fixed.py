val = 10
s = f'0b{val:04x}'  # '0b000a'
try:
    # Original: int(s[2:], 2) -> int('000a', 2) -> invalid
    result = int(s[2:], 2)
    print('Fmt slice result:', result)
except Exception as e:
    print('Fmt slice error:', type(e).__name__, str(e))
try:
    # Fix: int(s, 0) -> int('0b000a', 0) -> 10
    result2 = int(s, 0)
    print('Fmt fixed result:', result2)
except Exception as e:
    print('Fmt fixed error:', type(e).__name__, str(e))
# Now with % formatting
s2 = '0b%04x' % val
try:
    r1 = int(s2[2:], 2)
    print('%% slice:', r1)
except Exception as e:
    print('%% slice error:', type(e).__name__, str(e))
try:
    r2 = int(s2, 0)
    print('%% fixed:', r2)
except Exception as e:
    print('%% fixed error:', type(e).__name__, str(e))
# Show that slice gives different error than fixed
print('Slice was invalid base 2, fixed works')
