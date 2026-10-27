import functools, codecs
@functools.lru_cache()
def encode_and_write(text, encoding='utf-8'):
    data = text.encode(encoding)
    with open('tmp.dat', 'wb') as f:
        f.write(data)
        f.write(b'
')
    with open('tmp.dat', 'rb') as f:
        return f.read().strip(b'
')
result1 = encode_and_write('café')
result2 = encode_and_write('café')  # Should hit cache
print('First:', repr(result1))
print('Second:', repr(result2))
print('Equal:', result1 == result2)
import os; os.remove('tmp.dat') if os.path.exists('tmp.dat') else None
