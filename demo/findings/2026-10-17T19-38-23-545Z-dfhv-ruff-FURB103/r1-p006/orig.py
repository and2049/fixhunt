flag = False
with open('s.txt', 'w') as f:
    flag and f.write('should not happen')
with open('s.txt', 'r') as f:
    print(repr(f.read()))
import os; os.remove('s.txt')
