import os
from pathlib import Path
# Create a temporary file
open('tmp.txt', 'w').close()
try:
    # List comp that dict() wraps
    pairs = [(str(Path('tmp.txt')), os.path.abspath('tmp.txt')) for _ in range(1)]
    d = dict(pairs)
    print('Path str == abspath?', d[str(Path('tmp.txt'))] == d[os.path.abspath('tmp.txt')])
    # Now the dict comp equivalent (what rule would produce)
    d2 = {str(Path('tmp.txt')): os.path.abspath('tmp.txt') for _ in range(1)}
    print('dict comp same:', d2[str(Path('tmp.txt'))] == d2[os.path.abspath('tmp.txt')])
finally:
    os.remove('tmp.txt')
