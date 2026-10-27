text = 'café\n'
# Rule fires here: rewrites {c for c in text} to set(text)
chars = {c for c in text}
print(f'Chars from text: {sorted(chars)}')
# For bytes, similar issue
b = b'caf\xc3\xa9\n'
# Rule fires here: rewrites {c for c in b} to set(b)
byte_chars = {c for c in b}
print(f'Byte values: {sorted(byte_chars)}')
# Compare with direct set() calls
print(f'set(text):   {sorted(set(text))}')
print(f'set(b):      {sorted(set(b))}')
