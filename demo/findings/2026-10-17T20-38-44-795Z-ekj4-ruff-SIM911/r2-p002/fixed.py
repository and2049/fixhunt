d = {'a': b'hello\nworld', 'b': b'foo\r\nbar'}
pairs = list(d.items())
for k, v in pairs:
    print(k.decode(), v.decode().replace('\n', '\\n'))
