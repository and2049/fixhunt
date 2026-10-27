import sys

def f():
    x = 1
    y = 2
    z = x + y

frame = sys._getframe()
f()
offset = frame.f_lasti
print('offset:', offset)
if offset < 0:
    print('negative')
else:
    print('non-negative')
