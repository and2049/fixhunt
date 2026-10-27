import pathlib
flag = False
pathlib.Path('s.txt').write_text('should not happen')
with open('s.txt', 'r') as f:
    print(repr(f.read()))
import os; os.remove('s.txt')
