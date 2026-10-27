import typing
with open('test.bin', 'wb') as f:
    f.write(b'12345')
    f.seek(2)
    f.write(b'99')
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
