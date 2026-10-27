with open('test.txt', 'w') as f:
    f.write('hello')
    print(file=f)
    f.seek(0)
    f.write('world')
with open('test.txt') as f:
    print(repr(f.read()))
import os
os.remove('test.txt')
