import os
name = 'testfile'
with open(name, 'w') as f:
    f.write('data')
try:
    # Using os.path.exists - not(not(...)) form
    exists = bool(os.path.exists(name))
    print(f'os.path: {exists}')
    os.remove(name)
    # Second check after delete - would differ if duplicated
    exists2 = bool(os.path.exists(name))
    print(f'os.path after remove: {exists2}')
except Exception as e:
    print(f'OS error: {e}')
finally:
    if os.path.exists(name):
        os.remove(name)
