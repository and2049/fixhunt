cache = {}
def get_data(key):
    return cache.get(key, None)
for i in range(2):
    data = get_data('x')
    try:
        with open('tmp.bin', 'wb') as f:
            if data is None:
                data = b''
            f.write(data)
    except Exception as e:
        print(type(e).__name__, str(e))
import os
if os.path.exists('tmp.bin'):
    os.remove('tmp.bin')
