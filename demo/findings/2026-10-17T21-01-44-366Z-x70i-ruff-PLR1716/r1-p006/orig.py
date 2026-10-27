b = b'ab'
c = b'bc'
d = b'cd'
if b < c and c < d:
    print(b.decode())
else:
    print(b.decode()[::-1])
with open('test.txt', 'wb') as f:
    f.write(b'
')
with open('test.txt', 'rb') as f:
    data = f.read()
print(repr(data))
import os
os.remove('test.txt')
