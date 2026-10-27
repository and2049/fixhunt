with open('tmp.txt', 'w') as f:
    g = f
    g.write('hello')
with open('tmp.txt', 'r') as f:
    print(f.read())
import os; os.remove('tmp.txt')
