with open('tmp.txt', 'w') as f:
    f.write("first")
with open('tmp.txt', 'a') as f:
    f.write("second")
with open('tmp.txt', 'r') as f:
    print(f.read())
import os
os.remove('tmp.txt')
