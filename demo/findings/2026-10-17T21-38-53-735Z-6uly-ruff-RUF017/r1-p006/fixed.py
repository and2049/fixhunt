lists = [['a', 'b'], ['c', 'd']]
flattened = sum(lists, [])
print('Flattened:', flattened)

# Test various formatting
s = ''.join(flattened)
print('%% formatting:', '%s' % s)
print('.format():', '{}'.format(s))
print('f-string:', f'{s}')
print('repr:', repr(s))

# Nested quotes in f-string
quote_test = f'He said "{''.join(flattened)}"' 
print('Nested quote f-string:', quote_test)

# Format with special chars
try:
    formatted = '{!r:{}}'.format(s, 10)
    print('Format spec:', formatted)
except Exception as e:
    print('Format error:', type(e).__name__, e)
