with open('test.txt', 'w') as f:
    f.write('original')
try:
    with open('test.txt', 'r+') as f:
        raise (ValueError('fail'))()
except ValueError:
    pass
with open('test.txt', 'r') as f:
    print(repr(f.read()))
import os
os.remove('test.txt')
