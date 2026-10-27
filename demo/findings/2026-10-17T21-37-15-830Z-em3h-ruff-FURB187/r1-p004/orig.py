with open('test.bin', 'wb') as f:
    data = [b'\x00', b'\x01']
    f.write(bytes().join(data[::-1]))
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
