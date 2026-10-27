import string
with open('test.txt', 'w') as f:
    f.write(string.digits)
with open('test.txt', 'r') as f:
    content = f.read()
    print('read:', repr(content))
import os
os.remove('test.txt')
