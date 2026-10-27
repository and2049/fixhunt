for i in range(2):
    with open('log.txt', 'r') as f:  # trigger
        f.seek(0, 2)
        f.write(str(i) + '\n')
    with open('log.txt') as f:
        print(f.read(), end='')
import os; os.remove('log.txt')
