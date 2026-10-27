data = b'hello'
result = False if data == b'hello' else True
with open('test.txt', 'wb') as f:
    f.write(b'yes' if not result else b'no')
with open('test.txt', 'rb') as f:
    print('file contains:', f.read())
import os
os.remove('test.txt')
