open = lambda *a, **k: __builtins__.open(*a, **k)
path = 'shadow.txt'
with open(path, 'w') as f:
    f.write('test')
with open(path) as f:
    print(f.read())
import os
os.remove(path)
