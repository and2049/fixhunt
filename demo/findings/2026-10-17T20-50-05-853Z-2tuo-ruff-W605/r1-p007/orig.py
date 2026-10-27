import re
pattern = '\.'
text = 'a.b'
result = re.sub(pattern, 'X', text)
print(result)
print('expected: aXb')
if result == 'aXb':
    print('match')
else:
    print('mismatch:', repr(result))
