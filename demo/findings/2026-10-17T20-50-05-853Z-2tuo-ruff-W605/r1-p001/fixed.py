s = r'\.' 'rest'
t = s
print(repr(t))
if '__' in t:
    print('double backslash')
else:
    print('single backslash')
