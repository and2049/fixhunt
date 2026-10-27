from typing import TypeVar
T = TypeVar('T')
def process(data: T) -> T:
    with open('tmp.bin', 'wb') as f:
        f.write(data)  # Expects bytes
    return data
try:
    process(b'hello')
except TypeError as e:
    print('TypeError:', e)
finally:
    import os
    if os.path.exists('tmp.bin'):
        os.remove('tmp.bin')
