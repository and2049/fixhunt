with open('test.txt', 'w') as f:
    f.write('initial')

with open('test.txt', 'r+') as f:
    f.seek(0)
    data = f.read(1)  # read 'i'
    # Rule fires: f.write(data) if not data else f.write('X')
    # But we want to see if fix changes behavior
    # Instead: use ternary to decide what to write
    to_write = data if not data else 'X'  # data='i' -> truthy -> not data=False -> pick else: 'X'
    f.write(to_write)
    f.seek(0)
    content = f.read()
    print(f'content={repr(content)}')
import os
os.remove('test.txt')
