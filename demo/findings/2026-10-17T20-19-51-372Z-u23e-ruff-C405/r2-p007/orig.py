l = [b'hello
', b'world\r
']
s = set(l)
print(f'Set of byte strings: {s}')
for b in s:
    print(f'Bytes: {b!r}, Decoded: {b.decode()}')
