with open('tmp.txt', 'w') as f:
    pass
with open('tmp.txt', 'r+') as f:
    d = dict.fromkeys(['a','b'], f)
    d['a'].write('AB')
    f.seek(0)
    print(repr(f.read()))
import os; os.remove('tmp.txt')
