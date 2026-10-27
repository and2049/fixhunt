import functools

@functools.cache
def encode_string(s, encoding='utf-8'):
    return s.encode(encoding)

@functools.cache
def decode_bytes(b, encoding='utf-8'):
    return b.decode(encoding)

text = 'héllö'
encoded = encode_string(text)
decoded = decode_bytes(encoded)
print(f'Original: {repr(text)}')
print(f'Encoded: {repr(encoded)}')
print(f'Decoded: {repr(decoded)}')
print(f'Equal: {text == decoded}')
# Call again to hit cache
encoded2 = encode_string(text)
print(f'Same object: {encoded is encoded2}')
