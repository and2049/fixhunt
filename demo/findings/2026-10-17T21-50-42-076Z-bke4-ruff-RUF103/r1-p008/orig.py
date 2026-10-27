# Simulate writing to file where suppression fix alters byte count
import os
with open('test.txt', 'w') as f:
    f.write('# ruff: disable')  # exact bytes matter for truncation
size = os.path.getsize('test.txt')
print(f"File size: {size} bytes")
os.remove('test.txt')
