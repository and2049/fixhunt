import os
from pathlib import Path

# Create a temporary file
open('test.txt', 'w').close()
try:
    p = Path('test.txt')
    # Rule fires on next line
    exists_flag = p.exists() == True
    print('p.exists() == True:', exists_flag)
    # After rewrite: becomes p.exists()
    # Same value, but if we use it in 'is' check...
    print('p.exists() is True:', p.exists() is True)
    print('p.exists() == True is:', (p.exists() == True) is True)
finally:
    os.remove('test.txt')
