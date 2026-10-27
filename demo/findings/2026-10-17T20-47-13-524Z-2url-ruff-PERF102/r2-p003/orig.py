with open('test.txt', 'w') as f:
    pass
with open('test.txt', 'r+') as f:
    for k, v in {'a': 'hello', 'b': 'world'}.items():
        f.write(v)
        if k == 'a':
            f.truncate()
with open('test.txt', 'r') as f:
    print(repr(f.read()))
import os
os.remove('test.txt')
