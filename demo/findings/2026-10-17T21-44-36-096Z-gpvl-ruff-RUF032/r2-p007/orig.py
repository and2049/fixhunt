from decimal import Decimal
import os
filename = 'test_output.txt'
if os.path.exists(filename):
    os.remove(filename)
with open(filename, 'w') as f:
    f.write(str(Decimal(1.0 + 2.0)))
with open(filename, 'r') as f:
    content = f.read()
print(f'File content: {content!r}')
if os.path.exists(filename):
    os.remove(filename)
