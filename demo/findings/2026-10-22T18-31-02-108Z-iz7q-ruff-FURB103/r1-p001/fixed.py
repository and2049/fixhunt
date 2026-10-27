import os
import pathlib
counter = 0
def get_path():
    global counter
    counter += 1
    return f'test{counter}.txt'
pathlib.Path(get_path()).write_text('hello')
with open(get_path(), 'r') as f:
    print(f.read())
if os.path.exists('test1.txt'):
    os.remove('test1.txt')
if os.path.exists('test2.txt'):
    os.remove('test2.txt')
print(f'counter={counter}')
