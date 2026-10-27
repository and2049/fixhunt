import os

class H:
    base = '.'
    rel = 'test.txt'

with open(rel, 'w') as f:
    f.write('hello')

try:
    print('os.path exists:', os.path.exists(H.rel))
    print('pathlib exists:', os.path.exists(H.base + '/' + H.rel))
except Exception as e:
    print(type(e).__name__ + ':', str(e))
finally:
    if os.path.exists(H.rel):
        os.remove(H.rel)
