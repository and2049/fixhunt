prefix = 'ab'
s = 'abcde'
if s.startswith(prefix):
    s = s[len(prefix):]
print(s)
