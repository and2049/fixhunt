import os
def f():
    with open('test.txt', 'w') as fp:
        if True:
            return fp.write(b'hello')
    return None
with open('test.txt', 'r') as fp:
    print(repr(fp.read()))
os.remove('test.txt')
