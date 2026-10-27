try:
    not = 5  # SyntaxError: invalid syntax
except SyntaxError as e:
    print(type(e).__name__, e)
# Rule cannot fire on invalid syntax
print('Rule does not trigger due to syntax error')
