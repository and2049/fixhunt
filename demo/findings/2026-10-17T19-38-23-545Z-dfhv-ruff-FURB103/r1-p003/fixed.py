log = []
with open('x.txt', 'w') as f:
    log.append('start')
    f.write('data')
    log.append('end')
print(log)
with open('x.txt', 'r') as f:
    print(repr(f.read()))
import os; os.remove('x.txt')
