import sys
s = 'prefix'
p = 'pre'
if s.startswith(p):
    try:
        s = s.removeprefix(p)
    except AttributeError:
        s = s[len(p):]
print(s)
