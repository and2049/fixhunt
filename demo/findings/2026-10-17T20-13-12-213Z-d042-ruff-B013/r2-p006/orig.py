import os
try:
    with open('test.tmp', 'wb') as f:
        f.write(b'hello')
        raise OSError
except (OSError,) as e:
    with open('test.tmp', 'rb') as f:
        print(f.read())
finally:
    if os.path.exists('test.tmp'):
        os.remove('test.tmp')
