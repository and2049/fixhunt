name = 'Alice'
greeting = 'Hello %s #' % name
formatted = 'Hi {0}!'.format(name)
fstring = f'Hey {name} #'
print(greeting, formatted, fstring, sep='|')
