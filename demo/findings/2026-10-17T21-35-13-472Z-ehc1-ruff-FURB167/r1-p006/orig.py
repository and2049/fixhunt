import re
flags = re.I | re.L
pattern = r'\n'
string = 'a\nb'
print(re.findall(pattern, string, flags))
