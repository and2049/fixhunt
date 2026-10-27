def f():
    with open('test.bin', 'wb') as fp:
        fp.write(b'hello\nworld')
    with open('test.bin', 'rb') as fp:
        data = fp.read()
        if b'\n' in data:
            return data.replace(b'\n', b' ')

result = f()
print(result)
import os
os.remove('test.bin')
