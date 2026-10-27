data = b'hello
world'
print(data.decode())
with open('out.bin', 'wb') as f:
    f.write(data)
with open('out.bin', 'rb') as f:
    print(f.read())
import os
os.remove('out.bin')
