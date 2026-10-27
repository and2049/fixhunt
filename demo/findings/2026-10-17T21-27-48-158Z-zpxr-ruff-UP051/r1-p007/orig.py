import abc
import os
fname = 'test_file.txt'
if os.path.exists(fname):
    os.remove(fname)
@abc.abstractclassmethod
    def writer(cls):
        with open(fname, 'w') as f:
            f.write('first')
        with open(fname, 'a') as f:
            f.write('second')
writer.__func__(type('W', (), {}))
with open(fname, 'r') as f:
    content = f.read()
print('File content:', repr(content))
os.remove(fname)
