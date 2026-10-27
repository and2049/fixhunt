import os
os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('a\nb\nc')
with open('test.txt', 'r') as fp:
    for line in fp:
        if line.strip() == 'b':
            fp = open('test.txt', 'r')  # reassign fp
            fp.seek(0)
            next(fp)  # skip first line
            line2 = fp.readline().strip()
            print('After reassignment:', line2)
        print('Line:', line.strip())
os.remove('test.txt')
