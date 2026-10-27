import sys
d = {'a': 1}
for k, v in d.items():
    frame = sys._getframe(0)
    print('k' in frame.f_locals and 'v' in frame.f_locals, end='')
