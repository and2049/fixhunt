import re as regex
pattern = r'hello'
string = 'HELLO world'
if regex.search(pattern, string, regex.I):
    print('matched')
else:
    print('no match')
