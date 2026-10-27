import os
path_bytes = 'foo/bar'.encode('utf-8')
try:
    os.makedirs(path_bytes, exist_ok=True)
except TypeError:
    pass  # bytes not accepted directly in some versions
finally:
    decoded = os.fsdecode(path_bytes)
    print('decoded:', decoded)
