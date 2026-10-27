with open('test.bin', 'wb') as f:
    f.write(b'hello\n')
with open('test.bin', 'rb') as f:
    data = f.read()
print('bytes:', repr(data))
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')
with open('test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
print('text:', repr(data))
import os
os.remove('test.bin')
os.remove('test.txt')
