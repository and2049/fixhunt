data = b'hello'
if not data == 'hello':
    print('bytes not equal str')
else:
    print('bytes equal str (unexpected)')

if data != 'hello':
    print('bytes != str')
else:
    print('bytes == str (unexpected)')
