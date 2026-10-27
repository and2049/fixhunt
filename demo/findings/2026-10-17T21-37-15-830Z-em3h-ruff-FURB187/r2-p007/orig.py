b = b'hello\nworld'
b = b[::-1]
s = b.decode('utf-8')
print('reversed bytes:', b)
print('decoded string:', repr(s))
