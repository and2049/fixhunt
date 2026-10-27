import os
side = []
def get_data():
    side.append('called')
    return b'test'
with open('test.bin', 'wb') as f:
    print('before write')
    f.write(get_data())
print('after:', side)
os.remove('test.bin')
