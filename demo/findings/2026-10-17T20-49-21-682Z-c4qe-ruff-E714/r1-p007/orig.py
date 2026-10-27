b = b'hello'
s = 'hello'
print('Bytes check:', not b is b'hello')
print('Str check:', not s is 'hello')
print('Cross-type:', not b is s)
