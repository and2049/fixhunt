def log(msg, buf=[]):
    buf.append(msg)
    return buf
with open('log.txt', 'w') as f:
    f.write(str(log('first')))
with open('log.txt', 'r') as f:
    print(f.read())
import os; os.remove('log.txt')
