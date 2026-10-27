data = b'hello'
with open('test.bin', 'wb') as f:
    f.write(data[:])  # rule does not trigger on bytes
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
