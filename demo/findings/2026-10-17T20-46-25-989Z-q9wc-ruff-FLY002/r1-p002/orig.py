a = 'hello'
b = 'world'
expr = '-' + ' '.join((a, b)) + '-'
fexpr = '-' + f'{a} {b}' + '-'
print(expr == fexpr)
# Force different grouping via missing parentheses
x = 1
y = 2
z = 3
bad_join = '' + ''.join((str(x), str(y))) + str(z)
bad_fstring = '' + f'{x}{y}' + str(z)
print(bad_join, bad_fstring, sep='|')
