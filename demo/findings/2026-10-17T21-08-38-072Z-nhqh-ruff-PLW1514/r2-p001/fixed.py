import os

def my_open(*args, **kwargs):
    return open(*args, **kwargs)

try:
    f = my_open('test.txt', 'w')
    f.write('hi')
    f.close()
except TypeError as e:
    print('TypeError:', e)

with open('test.txt', 'w') as f:
    f.write('hello')

with open('test.txt', 'r') as f:
    print('Content:', f.read())

os.remove('test.txt')
