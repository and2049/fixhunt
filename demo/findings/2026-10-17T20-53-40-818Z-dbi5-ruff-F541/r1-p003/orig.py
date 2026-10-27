data = f"test"
with open('tmp.bin', 'wb') as f:
    f.write(data.encode())
with open('tmp.bin', 'rb') as f:
    print(f.read())
import os
os.remove('tmp.bin')
