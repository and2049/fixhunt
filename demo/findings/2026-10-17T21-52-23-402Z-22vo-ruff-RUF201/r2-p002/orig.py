msg = 'Error: %s'
code = "W291"  # trailing-whitespace -> ignore list entry
formatted = msg % code
print(formatted)
# Also testing f-string
print(f'Ignore: {code}')
# Nested quotes
s = "He said '%s'" % code
print(s)
