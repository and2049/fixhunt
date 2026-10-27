x = 1
mode = 'w' and [] and 'w'
data = x and [] and 'hello'
with open('test.txt', mode) as f:
    f.write(data)
with open('test.txt', 'r') as f:
    print('read:', repr(f.read()))
import os
os.remove('test.txt')
