import os
if os.path.exists('missing.txt'):
    os.remove('missing.txt')
try:
    with open('missing.txt', 'w') as f:
        f.write('should not happen')
except FileNotFoundError as e:
    print(f'Caught: {e}')
print('Done')
