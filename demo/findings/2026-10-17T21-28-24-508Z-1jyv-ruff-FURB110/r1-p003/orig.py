data = b'hello'
with open('test.bin', 'wb') as f:
    written = f.write(data) if written := f.tell() else 0
print('written:', written)
import os
os.remove('test.bin')
