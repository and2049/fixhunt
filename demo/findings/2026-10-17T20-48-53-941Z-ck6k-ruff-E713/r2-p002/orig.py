x = 5
y = [1, 2, 3]
# Rule does not trigger: embedded in expressions
print('%d' % (not x in y))
print('{}'.format(not x in y))
print(f'{not x in y}')
print(repr(not x in y))
