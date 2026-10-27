import typing
with open('test.bin', 'wb') as f:
    if typing.TYPE_CHECKING:
        pass
    f.write(b'hello' if not typing.TYPE_CHECKING else 'world')
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
