with open('test.txt', 'w') as f:
    f.write(r'\_')
with open('test.txt', 'r') as f:
    content = f.read()
print(repr(content))
import os
os.remove('test.txt')
