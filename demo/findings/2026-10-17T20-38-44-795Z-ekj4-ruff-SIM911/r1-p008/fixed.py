d = {b'a\nb': b'1\n2', b'c': b'3'}
zipped = list(d.items())
for k, v in zipped:
    print(repr(k), repr(v))
# Simulate text processing
try:
    for k, v in d.items():
        print(k.decode(), v.decode())
except Exception as e:
    print('Decode error:', type(e).__name__, str(e))
# Test newline handling
with open('test.txt', 'wb') as f:
    for k, v in d.items():
        f.write(k + b':' + v + b'\n')
with open('test.txt', 'rb') as f:
    print(f.read())
import os
os.remove('test.txt')
