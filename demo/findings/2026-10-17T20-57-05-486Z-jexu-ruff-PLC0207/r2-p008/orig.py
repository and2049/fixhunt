import os
open('test_file', 'w').close()
try:
    p = os.path.abspath('./test_file')
    name = p.split('/')[-1][:4]  # rule triggers on split('/')
    print(name)
finally:
    os.remove('test_file')
