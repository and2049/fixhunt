open('tmp.txt', 'w').write(f'first')
with open('tmp.txt', 'r+') as f:
    f.write(f'second')
    f.truncate()
with open('tmp.txt') as f:
    print(f.read())
import os; os.remove('tmp.txt')
