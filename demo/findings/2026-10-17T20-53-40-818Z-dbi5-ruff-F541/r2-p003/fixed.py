open('tmp.txt', 'w').write('first')
with open('tmp.txt', 'r+') as f:
    f.write('second')
    f.truncate()
with open('tmp.txt') as f:
    print(f.read())
import os; os.remove('tmp.txt')
