import re
flag = getattr(re, 'I')
pattern = r'hello'
string = 'HELLO'
print(bool(re.search(pattern, string, flag)))
