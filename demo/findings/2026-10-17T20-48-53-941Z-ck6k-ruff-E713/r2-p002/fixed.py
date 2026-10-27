x = 5
y = [1, 2, 3]
# Rule does not trigger: embedded in expressions
print('%d' % (x not in y))
print('{}'.format(x not in y))
print(f'{x not in y}')
print(repr(x not in y))
