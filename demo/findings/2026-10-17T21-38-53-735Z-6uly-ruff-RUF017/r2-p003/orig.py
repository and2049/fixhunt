import os
if os.path.exists('test.bin'):
    os.remove('test.bin')
with open('test.bin', 'wb') as f:
    chunks = [b'hello', b' ', b'world']
    written = sum(chunks, b'')  # flatten byte chunks
    f.write(written)
with open('test.bin', 'rb') as f:
    print(f.read())
if os.path.exists('test.bin'):
    os.remove('test.bin')
