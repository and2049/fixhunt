with open('test.txt', 'w') as f:
    f.write('0123456789')
with open('test.txt', 'r') as f:
    content = f.read()
    print('read:', repr(content))
import os
os.remove('test.txt')
