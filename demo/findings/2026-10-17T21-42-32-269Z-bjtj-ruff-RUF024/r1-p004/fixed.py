d = dict.fromkeys(['a','b'], ['{}'])
s = d['a'][0].format('X')
print(s)
