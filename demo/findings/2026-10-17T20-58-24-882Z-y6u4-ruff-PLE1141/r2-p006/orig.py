data = b'hello\nworld'
lines = data.split(b'\n')
print('Line count:', len(lines))
for i, line in enumerate(lines):  # No trigger: iterating list of bytes
    print(f'{i}: {line.decode()}')
