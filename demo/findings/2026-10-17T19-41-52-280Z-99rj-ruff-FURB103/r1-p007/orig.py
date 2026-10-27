def side_effect():
    print('Evaluating write arg')
    return 'data'
with open('tmp.txt', 'w') as f:
    f.write(side_effect())
with open('tmp.txt') as f:
    print(f.read())
import os
os.remove('tmp.txt')
