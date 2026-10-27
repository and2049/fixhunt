name = 'first.txt'
with open(name, 'w') as f:
    f.write('original')
name = 'second.txt'
with open(name, 'r') as f:
    print(f.read())
import os; os.remove('first.txt'); os.remove('second.txt')
