f = open('test.txt', 'w')
try:
    f.encoding = 'utf-8'
except: pass
f.write('line1\n')
f.write('line2')  # no newline yet
pos = f.tell()
f.close()
print('position before close:', pos)

f = open('test.txt', 'r')
content = f.read()
f.close()
print('content repr:', repr(content))
import os
os.remove('test.txt')
