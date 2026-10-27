r = 'wb'
with open('out.bin', r) as f:  # should NOT trigger
    f.write(b'hello')
with open('out.bin', 'rb') as f:
    print(f.read())
import os; os.remove('out.bin')
