import re
pattern = b'HELLO'
string = b'hello world'
print(re.findall(pattern, string, re.I))
