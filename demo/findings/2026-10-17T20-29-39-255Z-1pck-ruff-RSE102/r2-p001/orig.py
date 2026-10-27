import sys
try:
    exc = (ValueError,)
    raise exc
except SyntaxError as e:
    print('SyntaxError:', e.msg)
except ValueError as e:
    print('Caught:', type(e).__name__)
