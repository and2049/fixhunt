def wrapper(*a, **kw):
    return open(*a, **kw)
def forward(f, m='r'):
    return wrapper(f, mode=m)  # open(f, 'r') -> trigger
res = forward('tmp.txt')
res.write('x')
res.close()
with open('tmp.txt') as f:
    print(f.read())
import os; os.remove('tmp.txt')
