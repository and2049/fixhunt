f = open('test.bin', 'wb')
try:
    f.mode = 'wb'  # rule triggers
    f.write(b'hello')
    pos = f.tell()
    print('position after write:', pos)
except Exception as e:
    print('error during setattr/write:', type(e).__name__, ':', e)
f.close()

f2 = open('test.bin', 'rb')
print('file content:', f2.read())
f2.close()
import os
os.remove('test.bin')
