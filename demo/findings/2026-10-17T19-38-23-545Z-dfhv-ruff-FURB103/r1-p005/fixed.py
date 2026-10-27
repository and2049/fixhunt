import os
import pathlib
call_count = 0
def path():
    global call_count
    call_count += 1
    return 'p.txt'
pathlib.Path(path()).write_text(str(call_count))
with open('p.txt', 'r') as f:
    print(f.read())
print('path called:', call_count)
os.remove('p.txt')
