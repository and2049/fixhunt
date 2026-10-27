import os
os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('first\nsecond\nthird')
last_line = None
with open('test.txt', 'r') as fp:
    for line in fp.readlines():
        last_line = line
        if line.strip() == 'second':
            break
    print('In-loop last:', last_line.strip() if last_line else None)
    print('Is fp closed?', fp.closed)
print('Post-loop last:', last_line.strip() if last_line else None)
os.remove('test.txt')
