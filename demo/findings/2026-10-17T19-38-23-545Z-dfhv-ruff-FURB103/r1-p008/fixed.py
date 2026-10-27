import pathlib
def log(msg, buf=[]):
    buf.append(msg)
    return buf
pathlib.Path('log.txt').write_text(str(log('first')))
with open('log.txt', 'r') as f:
    print(f.read())
import os; os.remove('log.txt')
