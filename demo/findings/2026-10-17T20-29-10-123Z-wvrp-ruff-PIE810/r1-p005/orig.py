s = 'log'
if s.startswith('l') or s.startswith('lo'):
    with open('tmp.txt', 'w') as f:
        f.write('x')
        f.write('y')
with open('tmp.txt', 'r') as f:
    print(f.read())
import os
os.remove('tmp.txt')
