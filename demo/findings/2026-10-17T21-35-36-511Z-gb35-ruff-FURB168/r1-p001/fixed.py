data = b'hello\nworld\r\n'
txt = data.decode().replace('\r\n', '\n')
if txt is None:
    print('none')
else:
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(txt)
with open('test.txt', 'r', encoding='utf-8') as f:
    print(repr(f.read()))
import os; os.remove('test.txt')
