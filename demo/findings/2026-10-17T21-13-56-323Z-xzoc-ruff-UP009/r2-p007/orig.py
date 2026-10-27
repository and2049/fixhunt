# coding: utf-8
with open('test.bin', 'wb') as f:
    f.write(b'hazard')
    f.truncate(5)
with open('test.bin', 'rb') as f:
    print(f.read())
import os
os.remove('test.bin')
