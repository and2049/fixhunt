import os
try:
    os.remove('test.txt')
except FileNotFoundError:
    pass
p = 'test.txt'
if not os.path.exists(p) or open(p, 'w').close() and True:
    pass
else:
    print('fail')
if (not os.path.exists(p)) or (open(p, 'w').close() and True):
    pass
else:
    print('fail')
try:
    os.remove('test.txt')
except:
    pass
