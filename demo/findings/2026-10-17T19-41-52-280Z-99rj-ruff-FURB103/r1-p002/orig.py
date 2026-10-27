from typing import List
T = int
def get_data() -> T:
    return 42
with open('out.txt', 'w') as f:
    f.write(str(get_data()))
with open('out.txt') as f:
    print(f.read())
import os
os.remove('out.txt')
