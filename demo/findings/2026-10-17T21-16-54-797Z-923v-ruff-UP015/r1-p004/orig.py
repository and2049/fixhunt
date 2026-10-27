def log(msg, modes=['r']):
    with open('log.txt', modes[0]) as f:  # trigger: modes[0] is 'r'
        f.write(msg + '\n')
    modes.append('a')  # mutate default
log('first')
log('second')
with open('log.txt') as f:
    print(f.read(), end='')
import os; os.remove('log.txt')
