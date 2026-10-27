b = b'hello\nworld\n'
first_line = b.split(b'\n')[0].decode()
with open('out.txt', 'w') as f:
    f.write(first_line)
import os
os.remove('out.txt')
print(first_line)
