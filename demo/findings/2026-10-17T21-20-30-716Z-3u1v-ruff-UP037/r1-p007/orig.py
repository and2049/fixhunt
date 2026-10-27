def read_file(p: "str"):  # Rule may unquote to p: str
    with open(p, 'rb') as f:
        return f.read()
data = b'hello
world'
with open('test.bin', 'wb') as f:
    f.write(data)
result = read_file('test.bin')
print('bytes:', result)
import os
os.remove('test.bin')
