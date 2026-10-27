# fmt: off
with open('test.txt', 'wb') as f:
    f.write(b'hello')
    f.write(b'world')
with open('test.txt', 'rb') as f:
    print(f.read())
import os
os.remove('test.txt')
