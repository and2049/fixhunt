import os
import pathlib
counter = 0
def get_path():
    global counter
    counter += 1
    return 'tmp.txt'
try:
    pathlib.Path(get_path()).write_text(str(counter))
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
finally:
    if os.path.exists('tmp.txt'):
        with open('tmp.txt') as f:
            print(f'Read: {f.read()}')
        os.remove('tmp.txt')
print(f'Counter: {counter}')
