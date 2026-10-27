import os
import pathlib
# Create a temporary file
pathlib.Path('test.txt').write_text('hello')
try:
    # These do not involve Decimal, so rule does not fire
    p1 = pathlib.Path('test.txt')
    p2 = os.path.path('test.txt')  # AttributeError: module 'os' has no attribute 'path'
except AttributeError as e:
    print(f'{type(e).__name__}: {e}')
finally:
    try:
        os.remove('test.txt')
    except FileNotFoundError:
        pass
