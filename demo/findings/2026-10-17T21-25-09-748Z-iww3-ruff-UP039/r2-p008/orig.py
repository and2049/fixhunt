class E():
    f = open('tmp.txt', 'w')
    f.write('early')
    f.close()

with open('tmp.txt', 'r') as f:
    print(f.read())
import os; os.remove('tmp.txt')
del E
