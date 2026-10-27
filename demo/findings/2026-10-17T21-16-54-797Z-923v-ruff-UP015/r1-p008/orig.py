def read_config(path):
    """Read config file in text mode."""
    return open(path, 'r')  # explicit for clarity - trigger
with read_config('cfg.txt') as f:
    print(f.read())
with open('cfg.txt', 'w') as f:
    f.write('enabled=True')
import os; os.remove('cfg.txt')
