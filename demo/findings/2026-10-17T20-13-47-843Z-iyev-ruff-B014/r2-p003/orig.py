ValueError = 42  # shadows built-in
try:
    raise ValueError  # raises the variable (int), not exception
except (Exception, ValueError):  # linter sees two 'types', may dedupe
    print('Caught:', type(__import__('sys').exc_info()[1]))
    print('Value is:', ValueError)
except TypeError:
    print('Got TypeError as expected')
