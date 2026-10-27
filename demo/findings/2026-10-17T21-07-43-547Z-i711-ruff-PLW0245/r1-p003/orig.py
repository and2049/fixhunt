code = r'super.method()'
# This line contains super.method() — should NOT be changed
if 'super.method()' in code:
    print('found in string')
else:
    print('not found')
print(code)
