import pathlib
name = 'first.txt'
pathlib.Path(name).write_text('original')
name = 'second.txt'
with open(name, 'r') as f:
    print(f.read())
import os; os.remove('first.txt'); os.remove('second.txt')
