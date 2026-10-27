with open('test.txt', 'w') as f:
    while True:
        f.write(b'hello')  # bytes, not str
        break
with open('test.txt', 'rb') as f:
    data = f.read()
    print(data)
import os
os.remove('test.txt')
