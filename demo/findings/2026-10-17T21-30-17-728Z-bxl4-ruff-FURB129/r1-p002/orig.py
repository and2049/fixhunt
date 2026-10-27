import os
os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('x\ny\nz')
try:
    with open('test.txt', 'r') as fp:
        for line in fp.readlines():
            if line.strip() == 'y':
                raise ValueError('bad line')
            print('Read:', line.strip())
except ValueError as e:
    print('Caught:', type(e).__name__, str(e))
else:
    print('No exception')
finally:
    print('Finally block executed')
os.remove('test.txt')
