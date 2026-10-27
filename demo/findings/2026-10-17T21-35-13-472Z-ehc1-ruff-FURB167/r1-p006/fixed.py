import re
flags = re.IGNORECASE | re.LOCALE
pattern = r'\n'
string = 'a\nb'
print(re.findall(pattern, string, flags))
