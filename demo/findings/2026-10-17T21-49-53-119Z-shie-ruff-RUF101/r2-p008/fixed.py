data = eval('"hello"').encode()  # noqa: S307
with open('test.bin', 'wb') as f:
    f.write(data)
with open('test.bin', 'rb') as f:
    read = f.read()
print(read == b'hello')
import os
os.remove('test.bin')
