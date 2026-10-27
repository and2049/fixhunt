try:
    # This is a SyntaxError: cannot use 'not' before tuple unpacking in expression
    # We cannot put it in code directly; must be in a string or fail to parse.
    # Instead, demonstrate that such a line would be invalid.
    compile('not a, b in [1, 2, 3]', '<string>', 'eval')
except SyntaxError as e:
    print('SyntaxError:', type(e).__name__, '-', str(e))
# Valid contrast
print('normal:', not 1 in [1, 2, 3])
