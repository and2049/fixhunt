with open('tmp.txt', 'w') as f:
    f.write(f"first")
with open('tmp.txt', 'a') as f:
    f.write(f"second")
with open('tmp.txt', 'r') as f:
    print(f.read())
import os
os.remove('tmp.txt')
