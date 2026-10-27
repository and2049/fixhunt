x = 1
s = 'Result: {x}/3'
print('Before fix:', s.format(x=x))
print('After fix :', eval('f"' + s[1:-1] + '"'))
x = 2
print('Before fix:', s.format(x=x))
print('After fix :', eval('f"' + s[1:-1] + '"'))
