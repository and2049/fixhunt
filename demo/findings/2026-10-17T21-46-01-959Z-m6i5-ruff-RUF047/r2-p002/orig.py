data = b'hello'
if len(data) == 5:
    with open('out.bin', 'wb') as f:
        f.write(data)
else:
    pass
with open('out.bin', 'rb') as f:
    print(f.read())
import os
os.remove('out.bin')
