import functools
@functools.lru_cache
def cached_write(data):
    with open('tmp.bin', 'wb') as f:
        if isinstance(data, float):
            data = struct.pack('<d', data)
        elif isinstance(data, bool):
            data = b'\x01' if data else b'\x00'
        f.write(data[:2])  # Truncate to 2 bytes
        f.seek(0); return f.read()
try:
    result1 = cached_write(3.14)
    result2 = cached_write(True)
    print('float->bytes:', repr(result1))
    print('bool->bytes:', repr(result2))
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    import os; os.remove('tmp.bin') if os.path.exists('tmp.bin') else None
