with open('test.bin', 'wb') as f:
    f.write(b'hello')

with open('test.bin', 'rb') as f:
    data = f.read()
    if data is None:
        print('unreachable')
    else:
        print('read bytes:', data == b'hello')

import os
os.remove('test.bin')
