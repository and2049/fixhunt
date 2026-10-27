data = b'a
b\r
c
'
lines = []
for line in list(data):
    lines.append(chr(line))
print(''.join(lines))
