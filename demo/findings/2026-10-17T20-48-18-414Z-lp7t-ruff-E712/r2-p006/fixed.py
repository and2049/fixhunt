b = b'true'
s = 'true'
print('bytes == True:', b == True)
print('str == True:', s == True)
print('bool(bytes):', bool(b))
print('bool(str):', bool(s))
# Demonstrate that non-empty bytes/str are truthy despite != True
if b == True:
    print('Bytes equal True')
else:
    print('Bytes not equal True (but truthy)')
if s == True:
    print('Str equal True')
else:
    print('Str not equal True (but truthy)')
