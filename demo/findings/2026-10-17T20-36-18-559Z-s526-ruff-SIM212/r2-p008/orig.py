with open('test.bin', 'wb') as f:
    pass
data = b'hello' if not True else b'world'
with open('test.bin', 'wb') as f:
    f.write(data)
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
