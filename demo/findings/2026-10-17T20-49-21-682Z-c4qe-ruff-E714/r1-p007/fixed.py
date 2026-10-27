b = b'hello'
s = 'hello'
print('Bytes check:', b is not b'hello')
print('Str check:', s is not 'hello')
print('Cross-type:', b is not s)
