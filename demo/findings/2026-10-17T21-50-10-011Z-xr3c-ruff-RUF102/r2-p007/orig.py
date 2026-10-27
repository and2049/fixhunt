with open('test.bin', 'wb') as f:  # noqa: BADCODE
    f.write(b'hello')
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
