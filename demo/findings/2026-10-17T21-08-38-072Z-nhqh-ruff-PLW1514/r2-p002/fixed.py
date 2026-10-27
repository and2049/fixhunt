import tarfile
import os

with open('test.txt', 'w') as f:
    f.write('data')

with tarfile.open('test.tar', 'w') as tf:
    tf.add('test.txt')

try:
    with tarfile.open('test.tar', 'r', encoding='utf-8') as tf:
        pass
except TypeError as e:
    print('TypeError:', e)

os.remove('test.txt')
os.remove('test.tar')
