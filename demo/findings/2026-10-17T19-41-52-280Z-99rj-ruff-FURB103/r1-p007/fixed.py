import pathlib
def side_effect():
    print('Evaluating write arg')
    return 'data'
pathlib.Path('tmp.txt').write_text(side_effect())
with open('tmp.txt') as f:
    print(f.read())
import os
os.remove('tmp.txt')
