x = b'hello'
y = 'world'
print(isinstance(x, (bytes, str)), isinstance(y, (bytes, str)))
x = b'\xc3\xa9'
y = 'é'
print(isinstance(x, (bytes, str)), isinstance(y, (bytes, str)))
