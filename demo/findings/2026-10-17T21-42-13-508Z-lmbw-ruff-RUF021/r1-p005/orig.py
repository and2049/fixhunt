data = b'hello'
empty = b''
if data or empty and b'world':
    res = b'yes'
else:
    res = b'no'
print(res)
if data or (empty and b'world'):
    res = b'yes'
else:
    res = b'no'
print(res)
