import os
import pathlib
# Create a temporary file
with open('test.txt', 'w') as f:
    f.write('hello')

# Rule fires on int(len(...)) if we use len on something that is not plain int-compatible? No.
# Instead, we show int() on a path-derived int that is safe, but we use it in a loop
for i in range(2):
    if i == 0:
        l = int(len(os.path.abspath('test.txt')))
    else:
        l = int(len(str(pathlib.Path('test.txt').resolve())))
    print(f'Iter {i}: length = {l}')

# Cleanup
os.remove('test.txt')
